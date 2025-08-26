# backend/graph.py

import os
import logging
from dotenv import load_dotenv
from typing import Any, AsyncIterator, Dict

# LangChain and LangGraph imports
from langgraph.graph import StateGraph, END, START
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Import all our custom agent components ---

# The unified state for our graph
from backend.classes.state import AgentState 

# The Pydantic models for structured output
from backend.classes.state import VerseCodeSolution, CorrectingCodeSolution 

# The node classes we created
from backend.nodes.gen_verse_code_node import GenerationNode
from backend.nodes.correct_verse_code_node import CorrectionNode
from backend.nodes.build_check_node import BuildCheckNode
from backend.nodes.OutputParserNode import OutputParserNode

# RAG services
from backend.services.step1_rag_service import gen_RagService
from backend.services.step2_rag_service import correct_RagService

# Prompts
from backend.prompts.step1_system_prompt import step1_CODE_GENERATION_System_PROMPT_TEMPLATE
from backend.prompts.step1_user_prompt import step1_User_Template
from backend.prompts.step2_system_prompt import step2_CODE_Correct_System_PROMPT_TEMPLATE
from backend.prompts.step2_user_prompt import step2_Code_correct_user_prompt

# --- Configure Logging and Environment ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()
logger.info("Environment variables loaded if .env file exists.")


# =================================================================================
# AGENT CLASS
# =================================================================================

class CodeGenerationAgent:
    """
    Encapsulates the entire state, tools, and logic for the Verse code generation agent.
    This class sets up the graph and provides a simple interface to run it.
    """

    def __init__(self, websocket_manager=None, job_id=None,user_question=None,max_iterations=None):
        """
        Initializes the agent for a specific job, setting up all dependencies.
        """
        self.websocket_manager = websocket_manager
        self.job_id = job_id
        self.initial_state = AgentState(
            original_question=user_question,
            job_id=self.job_id,
            websocket_manager=self.websocket_manager,
            max_iterations=max_iterations,
            messages=[],
            iterations=0,
        )
        self._initialize_dependencies()
        self._build_graph()

    def _initialize_dependencies(self):
        """
        Private method to set up all chains, services, and node instances.
        """
        logger.info("Initializing agent dependencies...")
        
        # --- LLM Model ---
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro-preview-05-06",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.1,
        )

        # --- Generation Chain ---
        self.history_placeholder = MessagesPlaceholder(variable_name="chat_history")
        self.code_gen_prompt_template = ChatPromptTemplate.from_messages([
            ("system", step1_CODE_GENERATION_System_PROMPT_TEMPLATE),
            self.history_placeholder,
            ("user", step1_User_Template)], 
            template_format="jinja2")
        self.code_gen_chain = self.code_gen_prompt_template | self.model.with_structured_output(VerseCodeSolution)
        
        # --- Correction Chain ---
        self.code_correct_prompt_template = ChatPromptTemplate.from_messages([
            ("system", step2_CODE_Correct_System_PROMPT_TEMPLATE), 
            ("user", step2_Code_correct_user_prompt)
        ], template_format="jinja2")
        self.code_correct_chain = self.code_correct_prompt_template | self.model.with_structured_output(CorrectingCodeSolution)
        
        # --- Services ---
        self.gen_rag_service = gen_RagService()
        self.correct_rag_service = correct_RagService()
        
        # --- Nodes ---
        self.generator_node = GenerationNode(code_gen_chain=self.code_gen_chain, rag_service=self.gen_rag_service)
        self.correction_node = CorrectionNode(code_correct_chain=self.code_correct_chain, device_rag_service=self.correct_rag_service)
        self.build_check_node = BuildCheckNode()
        self.OutputParserNode = OutputParserNode()
        logger.info("All agent dependencies initialized.")

    def _build_graph(self):
        """
        Private method to construct and compile the StateGraph.
        """
        self.workflow = StateGraph(AgentState)
        
        # Add nodes
        self.workflow.add_node("generator", self.generator_node.run)
        # Using the name 'corrector' for clarity, as it runs the CorrectionNode
        self.workflow.add_node("corrector", self.correction_node.run)
        self.workflow.add_node("build_checker", self.build_check_node.run)
        self.workflow.add_node("OutputParserNode", self.OutputParserNode.run)

        # Define graph edges
        self.workflow.set_entry_point("generator")

        self.workflow.add_edge("generator", "corrector")
        self.workflow.add_edge("corrector", "build_checker")
        
        # This conditional edge now decides whether to loop for another attempt or proceed
        def decide_to_end_or_retry(state: AgentState):
            if state.get("build_error_flag"):
                logger.warning("Generation failed or requires retry. Checking iteration count.")
                if state.get("iterations", 0) >= state.get("max_iterations", 3):
                    logger.error("---MAX ITERATIONS REACHED, ENDING WORKFLOW---")
                    return "OutputParserNode"
                else:
                    logger.info("---CODE FAILED, ROUTING BACK TO GENERATOR FOR RETRY---")
                    return "generator"
            else:
                logger.info("---CODE GENERATED---")
                return "OutputParserNode"
        
        # The generator can either loop back on itself (if it fails) or go to the corrector
        self.workflow.add_conditional_edges(
            "build_checker",
            decide_to_end_or_retry,
            {
                "OutputParserNode": "OutputParserNode",
                "generator": "generator"
            }
        )
        self.workflow.add_edge("OutputParserNode", END)
        self.compiled_graph = self.workflow.compile()
        logger.info("LangGraph workflow compiled successfully.")



    async def run(self, thread: Dict[str, Any], user_question: str, max_iterations: int = 3) -> AsyncIterator[Dict[str, Any]]:
        """
        The public method to execute the agent's workflow. The name 'run' is kept
        to match the reference project's style.
        """
        initial_state = AgentState(
            original_question=user_question,
            job_id=self.job_id,
            websocket_manager=self.websocket_manager,
            max_iterations=max_iterations,
            messages=[],
            iterations=0,
        )
        logger.info(f"Starting agent stream for job_id: {self.job_id}")

        async for state in self.compiled_graph.astream(initial_state,thread):
            if self.websocket_manager and self.job_id:
                await self._handle_ws_update(state)
            yield state

    async def _handle_ws_update(self, state: Dict[str, Any]):
        """Handle WebSocket updates based on state changes"""
        update = {
            "type": "state_update",
            "data": {
                "current_node": list(state.keys())[0]
            }
        }
        await self.websocket_manager.broadcast_to_job(
            self.job_id,
            update
        )
    
    def compile(self):
        graph = self.compiled_graph
        return graph
    
   

