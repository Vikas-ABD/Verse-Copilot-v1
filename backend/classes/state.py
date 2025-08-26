# backend/agent/states.py

from typing import List, Dict, Any, TypedDict, Optional, NotRequired, Required

# Pydantic models are used for structured output from the LLM
from pydantic import BaseModel, Field

# This will be passed into the state to handle real-time communication
from backend.services.websocket_manager import WebSocketManager


# =================================================================================
# 1. PYDANTIC MODELS: For Structured LLM Output
#    These define the final, clean "product" that your agent generates.
# =================================================================================

class VerseCodeSolution(BaseModel):
    """
    Schema for a newly generated Verse code solution.
    This is the target structure for the `generate_verse_code_node`.
    """
    prefix: str = Field(description="A brief explanation of the Verse code solution and approach.")
    imports: str = Field(description="The necessary import statements for the Verse code. If no imports are needed, specify '# No imports needed'.")
    code: str = Field(description="The generated Verse code block itself, not including import statements.")
    devices_used: List[str] = Field(default_factory=list, description="List of unique device types (e.g., 'trigger_device') detected in the code.")
    events_used: List[str] = Field(default_factory=list, description="A list of events used, formatted as 'device_name.EventName'.")
    user_question_summary: str = Field(description="Concise summary of the user's problem to solve.")


class CorrectingCodeSolution(BaseModel):
    """
    Schema for a corrected Verse code solution.
    This could be used by a specialized correction node if you add one.
    """
    corrected_prefix: str = Field(description="A brief explanation of the corrections and the overall approach.")
    corrected_imports: str = Field(description="The fully corrected import statements for the Verse code.")
    corrected_code: str = Field(description="The fully corrected Verse code block itself.")




# =================================================================================
# 2. TYPEDDICT STATE: For LangGraph Workflow
#    This is the main state object that flows through your graph.
#    It holds all inputs, intermediate results, and communication tools.
# =================================================================================

class AgentState(TypedDict, total=False):
    """
    Represents the full state of the multi-step code generation agent's graph.
    """
    # === REQUIRED INPUTS ===
    original_question: str
    job_id: Optional[str]
    websocket_manager: Optional[Any]
    max_iterations: int

    # === RAG & CONTEXT ===
    rag_step1_context: Optional[str]
    rag_step2_context: Optional[str]
    
    # === LLM INTERACTION ===
    messages: List[Dict[str, Any]]
    
    # === GENERATION & REFINEMENT LOOP ===
    iterations: int

    # devices and events for verse code
    devices_used: Optional[List[str]]
    events_used: Optional[List[str]] 
    
    # Store the full structured output at each major step
    draft_solution_verse_code: Optional[str]      # Holds a VerseCodeSolution from step 1
    refined_solution_verse_code: Optional[str]    # Holds a VerseCodeSolution from step 2
    
    # Specific feedback from a validation/build node
    build_error_feedback: Optional[str]
    build_error_flag: bool

    # === FINAL RESULT ===
    # The final, ready-to-use code string, extracted from the last successful solution
    final_code: str