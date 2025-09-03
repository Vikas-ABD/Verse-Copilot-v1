
# backend/app.py
import asyncio
import logging
import os
import uuid
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, BackgroundTasks,status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from langgraph.graph import END
from vector_store_manager import load_all_vector_stores
from backend.services.youtube_service import process_youtube_url
# --- NEW: Import StaticFiles ---
from fastapi.staticfiles import StaticFiles

# --- Import your Agent and WebSocket Manager ---
try:
    from backend.graph import CodeGenerationAgent as Graph
    from backend.services.websocket_manager import WebSocketManager
except ImportError as e:
    print(f"Error importing agent components: {e}")
    print("Please ensure you are running from the root 'Code_Agent' directory and all files are correctly placed.")
    exit(1)

from backend.services.update_KB_step1_service import AddKnowledgeBaseService1

# --- Basic Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()

# --- FastAPI App Initialization ---
app = FastAPI(title="Verse Code Generation Agent API......")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#------Loading Vector stores------------
load_all_vector_stores()

# --- Singleton Instances ---
manager = WebSocketManager()
job_statuses = defaultdict(lambda: {"status": "pending", "result": None, "error": None})


# --- Pydantic Models for API Requests ---
class GenerationRequest(BaseModel):
    user_question: str

class KnowledgeBase1Request(BaseModel):
    question: str = Field(..., description="The natural language question or use-case for the code.")
    verse_code: str = Field(..., description="The corresponding Verse code snippet.")

# --- NEW: Pydantic Model for the new YouTube Route ---
class YouTubeSummarizationRequest(BaseModel):
    youtube_url: str = Field(..., description="The URL of the YouTube video to summarize.")


# --- Background Task to Run the Agent ---
async def process_code_generation(job_id: str, request: GenerationRequest):
    """
    This function runs in the background, creating an agent instance and
    executing its `run` method.
    """
    logger.info(f"Starting agent processing for job_id: {job_id}")
    job_statuses[job_id] = {"status": "processing", "result": None, "error": None}
    
    final_state_result = None
    try:
        agent = Graph(
            websocket_manager=manager, 
            job_id=job_id
        )

        final_state_result = None  # Initialize to None before the loop

        # This loop will run for every step in the graph
        async for state_update in agent.run(user_question=request.user_question, max_iterations=3, thread={}):
            #logger.info(f"my states:--------------------{state_update}")
            final_state_result = state_update

        if final_state_result:
            final_code=final_state_result["OutputParserNode"].get("final_code")
            logger.info(f"Job {job_id} completed successfully.")
            job_statuses[job_id] = {"status": "completed", "result": final_code}
            await manager.broadcast_to_job(job_id, {
                "type": "final_result",
                "data": {"status": "complete", "final_code": final_code}
            })
        else:
            # This will handle the case where the graph ended but final_code wasn't produced
            # (e.g., max iterations were reached)
            error_message = "Agent finished, but no final code was generated."
            if final_state_result:
                error_message = final_state_result.get("build_error_feedback", error_message)
                
            logger.error(f"Job {job_id} failed: {error_message}")
            await manager.broadcast_to_job(job_id, {
                "type": "error",
                "data": {"status": "failed", "message": error_message}
            })


    except Exception as e:
        logger.error(f"Error processing job {job_id}: {e}", exc_info=True)
        error_message = f"An error occurred: {e}"
        job_statuses[job_id] = {"status": "failed", "error": error_message}
        await manager.broadcast_to_job(job_id, {
            "type": "error",
            "data": {"status": "failed", "message": error_message}
        })


# --- API Endpoints ---

@app.post("/generate-code", summary="Start Code Generation Job")
async def generate_code(request: GenerationRequest, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    logger.info(f"Received generation request. Assigned job_id: {job_id}")
    
    background_tasks.add_task(process_code_generation, job_id, request)
    
    return {
        "message": "Code generation process started. Connect to the WebSocket for real-time updates.",
        "job_id": job_id,
        "websocket_url": f"/ws/status/{job_id}"
    }


@app.websocket("/ws/status/{job_id}")
async def websocket_status_endpoint(websocket: WebSocket, job_id: str):
    await websocket.accept()
    
    await manager.connect(websocket, job_id)
    logger.info(f"Client connected to WebSocket for job_id: {job_id}")
    try:
        if job_id in job_statuses:
             await websocket.send_json({
                 "type": "connection_ack",
                 "data": {"current_status": job_statuses[job_id]}
            })
        
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket, job_id)
        logger.info(f"Client disconnected from WebSocket for job_id: {job_id}")
    except Exception as e:
        logger.error(f"WebSocket error for job {job_id}: {e}", exc_info=True)
        manager.disconnect(websocket, job_id)



@app.post("/add-knowledge1", summary="Add a new entry to the step1 Knowledge Base")
async def add_knowledge1_entry(entry: KnowledgeBase1Request):
    """
    Receives a question and a Verse code snippet and adds it as a new
    document to the FAISS vector database.
    """
    #logger.info(f"Received request to add new knowledge entry. Question: '{entry.question[:30]}...'")
    
    # 1. Instantiate your service
    service = AddKnowledgeBaseService1()
    
    # 2. Convert the Pydantic model to a dictionary and call the service
    #    The .model_dump() method is the modern equivalent of .dict()
    data_dict = entry.model_dump()
    success = await service.add_entry(data_dict)
    
    # 3. Respond based on the outcome
    if success:
        # Return a success response with a 201 Created status code
        return {
            "status": "success",
            "message": "The new knowledge has been successfully added to the database."
        }
    else:
        # If the service returns False, raise an HTTP exception
        # This gives a more accurate error response to the client
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add the entry to the knowledge base. Check server logs for details."
        )




# # --- NEW: YouTube Summarization Endpoint ---
# @app.post("/summarize-youtube-video", summary="Generate a summary from a YouTube URL")
# async def summarize_youtube_video(request: YouTubeSummarizationRequest):
#     """
#     Receives a YouTube URL, generates a summary using the Gemini API,
#     and returns the summary.
#     """
#     logger.info(f"Received request to summarize YouTube URL: {request.youtube_url}")

#     try:
#         # Call the async function from our new service file
#         summary_text = await  process_youtube_url(request.youtube_url)

#         # Return the successful response
#         return {
#             "status": "success",
#             "youtube_url": request.youtube_url,
#             "summary": summary_text
#         }
#     except Exception as e:
#         # Catch potential exceptions from the API call and return a proper HTTP error
#         logger.error(f"Failed to summarize video. Error: {e}", exc_info=True)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Failed to generate video summary. Error: {str(e)}"
#         )
    


# --- NEW: YouTube Summarization WebSocket ---
@app.websocket("/ws/summarize-youtube-video")
async def summarize_youtube_video_ws(websocket: WebSocket):
    """
    WebSocket endpoint for summarizing YouTube videos.
    Expects a JSON payload: {"youtube_url": "<url>"}
    """
    await websocket.accept()
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_json()
            youtube_url = data.get("youtube_url")

            if not youtube_url:
                await websocket.send_json({
                    "status": "error",
                    "message": "Missing 'youtube_url' in request"
                })
                continue

            logger.info(f"Received request to summarize YouTube URL: {youtube_url}")

            try:
                # Send acknowledgment
                await websocket.send_json({
                    "status": "processing",
                    "message": f"Started Working on  {youtube_url}"
                })

                # Process the YouTube video
                summary_text = await process_youtube_url(youtube_url)

                # Send the summary back
                await websocket.send_json({
                    "status": "success",
                    "youtube_url": youtube_url,
                    "summary": summary_text
                })

            except Exception as e:
                logger.error(f"Failed to summarize video. Error: {e}", exc_info=True)
                await websocket.send_json({
                    "status": "error",
                    "message": f"Failed to generate summary. Error: {str(e)}"
                })

    except WebSocketDisconnect:
        logger.info("WebSocket connection closed by client")




# --- NEW: Mount the static directory to serve the frontend ---
# This must come AFTER all your API routes.
if os.path.isdir('static'):
   app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
