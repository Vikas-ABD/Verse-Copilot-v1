# backend/services/add_knowledge_base_service.py

import logging
from typing import Dict, Any

# Import the specific async utility function we need
from backend.utils.update_KB_step1_utils import add_to_knowledge_base_async

logger = logging.getLogger(__name__)

class AddKnowledgeBaseService1:
    """
    A dedicated service for adding new entries to the knowledge base.
    
    This class provides a clean, high-level interface for the "add" operation,
    delegating the complex interaction with the vector database to utility functions.
    """

    def __init__(self):
        """
        Initializes the AddKnowledgeBaseService.
        There is no heavy initialization needed here as the utility function
        handles loading the DB on each call.
        """
        logger.info("Initialized AddKnowledgeBaseService.")
        pass

    async def add_entry(self, data: Dict[str, Any]) -> bool:
        """
        Processes the request to add a new data entry to the FAISS vector DB.

        Args:
            data: A dictionary containing the 'question' and 'verse_code'
                  for the new knowledge base entry.

        Returns:
            True if the entry was added successfully, otherwise False.
        """
        logger.info("Service received request to add a new knowledge entry.")
        try:
            # Await the utility function that performs the core logic
            success = await add_to_knowledge_base_async(data)
            if success:
                logger.info("Successfully added entry to the knowledge base.")
            else:
                logger.warning("Failed to add entry to the knowledge base.")
            return success
        except Exception as e:
            # Catch any unexpected errors from the utility function
            logger.error(f"An unexpected error occurred in the add_entry service: {e}")
            return False
