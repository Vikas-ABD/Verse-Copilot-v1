# invoke_test.py

import asyncio
import logging
import uuid
import json

# --- Import the Agent class ---
try:
    from backend.graph import CodeGenerationAgent
    from backend.classes.state import AgentState
except ImportError:
    print("Error: Could not import agent components.")
    print("Please make sure you are running this script from the root 'Code_Agent' directory.")
    exit(1)

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def run_agent_for_question(question: str):
    """
    Instantiates the agent and invokes the entire graph,
    printing only the final result.
    """
    job_id = f"invoke-job-{uuid.uuid4()}"
    logger.info(f"--- New Run --- Job ID: {job_id} ---")

    # 1. Instantiate the Agent
    agent = CodeGenerationAgent(websocket_manager=None, job_id=job_id)

    # 2. Create the initial state dictionary to pass to the graph
    initial_state = AgentState(
        original_question=question,
        job_id=job_id,
        websocket_manager=None,
        max_iterations=3,
        messages=[],
        iterations=0,
    )

    # 3. Invoke the entire graph from start to finish
    # .ainvoke() runs the whole process and returns only the final state.
    print("\nInvoking agent... please wait for the final result.")
    final_state = await agent.workflow.compile().ainvoke(initial_state)
    print("Agent finished execution.")


    # --- Print the final result ---
    print("\n" + "="*60)
    logger.info("--- AGENT WORKFLOW COMPLETE ---")
    print("="*60)

    if final_state:
        print("\n✅ Final State Object (All Fields):\n")
        # Pretty-print the entire final state dictionary
        print(json.dumps(final_state, indent=2))
        
        # Also print the final code separately for clarity
        final_code = final_state.get('final_code')
        if final_code:
            print("\n✅ Final Generated Verse Code:\n")
            print("-" * 30)
            print(final_code)
            print("-" * 30)
        else:
            print("\n❌ Agent finished, but the 'final_code' field was not in the final state.")
    else:
        print("\n❌ Agent finished unexpectedly. No final state was returned.")


async def main():
    """
    The main loop to continuously ask for user input and run the agent.
    """
    while True:
        print("\n" + "="*60)
        print("Enter your Verse code question below (or 'exit' to stop):")
        print("="*60)
        
        try:
            user_question = input("> ")
            if user_question.lower() in ["exit", "quit"]:
                print("Exiting test script. Goodbye!")
                break
            if not user_question:
                continue

            await run_agent_for_question(user_question)

        except Exception as e:
            logger.error(f"An error occurred during the agent run: {e}", exc_info=True)


if __name__ == "__main__":
    try:
        print("Starting Interactive Agent Test Script (Invoke Mode)...")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("\nTest script interrupted by user.")