# backend/agent/nodes/refinement.py

import logging
from langchain_core.runnables import Runnable

# Import the RAG service specialized for fetching device context
from backend.services.step2_rag_service import correct_RagService

# Import the state and Pydantic models
from backend.classes.state import AgentState, CorrectingCodeSolution

# Set up logging
logger = logging.getLogger(__name__)

class  CorrectionNode:
    """
    A self-contained node responsible for:
    1. Analyzing a draft code solution to identify devices used.
    2. Fetching specific RAG context for those devices.
    3. Invoking a correction/refinement LLM chain to improve the code.
    4. Saving the final, polished code to the agent's state.
    """

    def __init__(self, code_correct_chain: Runnable, device_rag_service: correct_RagService):
        """
        Initializes the node with its required dependencies.
        
        Args:
            code_correct_chain: An initialized LangChain runnable for correcting and refining Verse code.
            device_rag_service: A service object for fetching context about specific Verse devices.
        """
        self.code_correct_chain = code_correct_chain
        self.device_rag_service = device_rag_service

    async def refine(self, state: AgentState) -> dict:
        """
        The core logic for the code refinement process.
        """
        logger.info("---NODE: REFINING AND CORRECTING CODE SOLUTION---")
        
        draft_solution_verse_code = state.get("draft_solution_verse_code")
        if not draft_solution_verse_code:
            logger.error("---ERROR in RefinementNode: No draft solution found in state.---")
            return {"build_error_flag": True, "build_error_feedback": "Cannot refine code; no draft solution exists."}

        # Extract the draft code and the list of devices from the previous step's solution
        devices_used = state.get("devices_used", [])
        events_used = state.get("events_used", [])
        # --- 1. Fetch Device-Specific RAG Context ---
        #logger.info(f"Fetching device context for: {devices_used}")
        
        try:
            # The service takes the list of devices and returns relevant documentation/examples
            device_context = await self.device_rag_service.fetch_device_context(devices_used)
            logger.info("Successfully fetched device-specific context.")
        except Exception as e:
            logger.error(f"---ERROR in Device RAG Service: {e}---", exc_info=True)
            return {"build_error_flag": True, "build_error_feedback": f"Failed to retrieve device context: {e}"}

        # --- 2. Prepare for LLM Refinement ---
        # --- 3. Invoke the Correction Chain ---
        try:
            # Using the exact keys from your chain definition
            # The output should be a `CorrectingCodeSolution` Pydantic model
            corrected_solution: CorrectingCodeSolution = await self.code_correct_chain.ainvoke({
                "Generated_Verse_Code": draft_solution_verse_code,
                "Device_Context": device_context
            })
            
            # --- 4. Process the Output and Prepare State Update ---
            logger.info("---SUCCESS: Code refinement complete---")

            # Combine the corrected imports and code into the final version
            corrected_verse_code = f"{corrected_solution.corrected_imports}\n{corrected_solution.corrected_code}"

            # Construct the final state update
            updated_state = {
                "final_code": corrected_verse_code,
                "build_error_flag": False,
                "build_error_feedback": ""
            }

            return updated_state

        except Exception as e:
            logger.error(f"---ERROR in Correction LLM: {e}---", exc_info=True)
            return {"build_error_flag": True, "build_error_feedback": f"The code correction model failed to run: {e}"}

    async def run(self, state: AgentState) -> dict:
        """
        The public entry point for the graph.
        """
        # Unlike the generation node, this one doesn't manage iteration counts itself.
        # It's a distinct step in the workflow.
        return await self.refine(state)