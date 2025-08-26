# test_ws.py

import asyncio
import websockets
import json
import httpx  # A modern, async-capable HTTP client
import logging

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - CLIENT - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- API Configuration ---
BASE_URL = "http://127.0.0.1:8000"
API_ENDPOINT = f"{BASE_URL}/generate-code"
WS_URL_TEMPLATE = "ws://127.0.0.1:8000/ws/status/{job_id}"


async def start_generation_job(client: httpx.AsyncClient, question: str) -> str | None:
    """Sends a POST request to start the agent job and returns the job ID."""
    try:
        logger.info("Sending request to start generation job...")
        response = await client.post(API_ENDPOINT, json={"user_question": question}, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        data = response.json()
        job_id = data.get("job_id")
        logger.info(f"Job started successfully. Job ID: {job_id}")
        return job_id
        
    except httpx.RequestError as e:
        logger.error(f"HTTP request failed: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred when starting the job: {e}")
    return None


async def listen_for_updates(job_id: str):
    """Connects to the WebSocket and prints all incoming status updates."""
    ws_url = WS_URL_TEMPLATE.format(job_id=job_id)
    logger.info(f"Connecting to WebSocket at: {ws_url}")
    
    try:
        async with websockets.connect(ws_url) as websocket:
            logger.info("WebSocket connection established. Waiting for updates...")
            # This loop will run until the server closes the connection or we break it
            async for message in websocket:
                data = json.loads(message)
                
                # Nicely format and print the structured update from the server
                print("\n" + "-"*20 + " [WebSocket Update] " + "-"*20)
                
                msg_type = data.get("type", "unknown")
                msg_data = data.get("data", {})
                
                # The _handle_ws_update in your agent sends this type
                if msg_type == "state_update":
                    node = msg_data.get('current_node', 'N/A')
                    print(f"  Node '{node}' finished.")
                # The process_code_generation function sends this on success
                elif msg_type == "final_result":
                    print("  🎉 Final Result Received!")
                    print(json.dumps(msg_data, indent=2))
                    final_code = msg_data.get("final_code", "")
                    if final_code:
                        with open("output.verse", "w", encoding="utf-8") as f:
                            f.write(final_code)
                        print("✅ Code successfully written to 'output.verse'.")
                    else:
                        print("⚠️ No 'final_code' field found in result.")
                    break # Exit the loop once we get the final result
                # The process_code_generation function sends this on failure
                elif msg_type == "error":
                    print("  ❌ An error occurred!")
                    print(json.dumps(msg_data, indent=2))
                    break # Exit on error
                else:
                    # Print any other message types directly for debugging
                    print(json.dumps(data, indent=2))
                    
                print("-" * 58)

            logger.info("Final message received. Closing WebSocket.")

    except websockets.exceptions.ConnectionClosed as e:
        logger.warning(f"WebSocket connection closed by server: {e}")
    except Exception as e:
        logger.error(f"An error occurred with the WebSocket connection: {e}")


async def main():
    """Main function to run the interactive test loop."""
    async with httpx.AsyncClient() as client:
        while True:
            print("\n" + "="*60)
            print("Enter your Verse code question below (or 'exit' to stop):")
            print("="*60)
            
            question = input("> ")
            if question.lower() in ["exit", "quit"]:
                break
            if not question:
                continue

            # Step 1: Start the job via HTTP POST
            job_id = await start_generation_job(client, question)

            # Step 2: If job started, connect to WebSocket and listen
            if job_id:
                await listen_for_updates(job_id)


if __name__ == "__main__":
    try:
        print("Starting FastAPI WebSocket Test Client...")
        print("Please ensure your FastAPI server (`backend/app.py`) is running in another terminal.")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("\nClient stopped by user.")