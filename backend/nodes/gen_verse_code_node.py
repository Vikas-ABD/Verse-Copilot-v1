# backend/agent/nodes/generation.py

import logging
from langchain_core.runnables import Runnable

# We need a placeholder for the RAG service that will be injected.
from backend.services.step1_rag_service import gen_RagService 

# Import the state and Pydantic models
from backend.classes.state import AgentState, VerseCodeSolution

# Set up logging
logger = logging.getLogger(__name__)

class GenerationNode:
    """
    A self-contained node that handles RAG and conversational code generation.
    It can learn from validation feedback and retry.
    """

    def __init__(self, code_gen_chain: Runnable, rag_service: gen_RagService ):
        """
        Initializes the node with its required dependencies.
        
        Args:
            code_gen_chain: An initialized LangChain runnable that includes a MessagesPlaceholder.
            rag_service: A service object for fetching RAG context.
        """
        self.code_gen_chain = code_gen_chain
        self.rag_service = rag_service

    async def generate(self, state: AgentState) -> dict:
        """
        The core logic for the generation process.
        """
        logger.info("---NODE: GENERATING CODE SOLUTION---")
        
        question = state["original_question"]
        messages = state.get("messages", []) # Get the current message history
        
        # --- 1. Fetch RAG Context (only on the first attempt) ---
        # On retries, we assume the context is still relevant.
        if state.get("iterations", 0) <= 1:
            logger.info("First attempt: Fetching RAG context...")
            try:
                rag_context = await self.rag_service.fetch_context(question)
                logger.info("Successfully fetched RAG context.")
            except Exception as e:
                logger.error(f"---ERROR in RAG Service: {e}---", exc_info=True)
                return {"build_error_flag": True, "build_error_feedback": f"Failed to retrieve context: {e}"}
        else:
            # Use the context from the previous state on retries
            rag_context = state.get("rag_step1_context", "")

        # --- 2. Prepare for LLM Generation ---
        # *** KEY CHANGE: ADD VALIDATION FEEDBACK TO THE MESSAGE HISTORY ***
        if state.get("build_error_flag"):
            feedback = state.get("build_error_feedback", "An unknown error occurred.")
            # Add the corrective feedback as a new "user" message.
            # This tells the model what it did wrong in the previous turn.
            feedback_message = {
                "role": "user",
                "content": f"Your previous code attempt failed with the following error: '{feedback}'. Please analyze the error and provide a new, corrected code solution."
            }
            messages.append(feedback_message)
            logger.info("Appended validation feedback to message history for retry.")

        # --- 3. Invoke the Generation Chain ---
        try:
            # The chain now accepts "chat_history" which is filled by the MessagesPlaceholder
            code_solution: VerseCodeSolution= await self.code_gen_chain.ainvoke({
                "user_question": question,
                "helper_context": rag_context,
                "chat_history": messages # Pass the entire conversation history
            })
            
            # --- 4. Process the Output and Prepare State Update ---
            logger.info("---SUCCESS: Code generation complete---")

            # Add the AI's successful response to the history for the *next* potential loop
            assistant_response = {
                "role": "assistant",
                "content": f"Prefix: {code_solution.prefix}\nImports: {code_solution.imports}\nCode: {code_solution.code}"
            }
            messages.append(assistant_response)
            
            # Combine imports and code for the validator
            full_draft_code = f"\n{code_solution.imports}\n{code_solution.code}"
            
            updated_state = {
                "messages": messages, # Return the UPDATED message list
                "rag_step1_context": rag_context,
                "draft_solution_verse_code": full_draft_code,
                "devices_used": code_solution.devices_used,
                "events_used": code_solution.events_used,
                "build_error_flag": False,
                "build_error_feedback": "",
            }
            return updated_state

        except Exception as e:
            logger.error(f"---ERROR in Generation LLM: {e}---", exc_info=True)
            return {"build_error_flag": True, "build_error_feedback": f"The code generation model failed to run: {e}"}

    async def run(self, state: AgentState) -> dict:
        """
        The public entry point for the graph. Calls the main logic and updates the iteration count.
        """
        iterations = state.get("iterations", 0) + 1
        
        generation_result = await self.generate(state)
        
        generation_result["iterations"] = iterations
        
        return generation_result
