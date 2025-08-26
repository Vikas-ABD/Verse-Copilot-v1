import logging

logger = logging.getLogger(__name__)

class OutputParserNode:
    """
    A node that validates the final generated code.
    If the code is empty, it replaces it with a user-friendly error message.
    """
    def run(self, state: dict) -> dict:
        """
        Takes the current state and checks the 'final_code'.

        Args:
            state: The current state of the agent, expected to be a dictionary.

        Returns:
            A dictionary with updates for the state.
        """
        logger.info("---PARSING FINAL OUTPUT---")
        
        final_code = state.get("final_code")
        user_facing_error = "We are facing a technical issue now, please try again."

        # Check if final_code exists and is not just empty spaces
        if final_code:
            logger.info("---VALIDATION SUCCESS: Final code is not empty.---")
            # No changes to the state are needed if validation is successful
            return {"final_code":final_code}
        else:
            logger.error("---Validation Failed: 'final_code' was empty. Replacing with error message.---")
            # Overwrite the empty final_code with the user-facing error message
            return {"final_code": user_facing_error}