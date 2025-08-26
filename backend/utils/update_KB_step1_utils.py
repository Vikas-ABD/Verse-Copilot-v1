# backend/utils/knowledge_base_utils.py

import os
import logging
import asyncio
from typing import Dict, Any

from langchain.schema.document import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# --- Basic Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()

# --- Global Configuration ---
DB_PATH = "faiss_index"
MODEL_NAME = "models/text-embedding-004"

# --- Embedding Model Initialization ---
try:
    embeddings = GoogleGenerativeAIEmbeddings(model=MODEL_NAME)
except Exception as e:
    logger.critical(f"Fatal: Could not initialize embeddings. Check GOOGLE_API_KEY. Error: {e}")
    embeddings = None

def _add_to_faiss_sync(doc_to_add: Document, db_path: str, embeddings_model: GoogleGenerativeAIEmbeddings):
    """
    Synchronous helper function to perform blocking I/O operations.
    It loads the FAISS index, adds a new document, and saves it back to disk.
    This function is designed to be run in a separate thread.
    """
    try:
        # Load the existing vector store from the specified path
        logger.info(f"Loading FAISS index from '{db_path}' for update...")
        vector_store = FAISS.load_local(
            db_path,
            embeddings_model,
            allow_dangerous_deserialization=True
        )

        # Add the new document to the in-memory index
        logger.info(f"Adding new document to index...")
        vector_store.add_documents([doc_to_add])

        # Save the updated index back to the same location
        logger.info(f"Saving updated index back to '{db_path}'...")
        vector_store.save_local(db_path)
        logger.info("✅ Index updated and saved successfully.")
        return True

    except FileNotFoundError:
        logger.error(f"❌ FAISS database not found at '{db_path}'. Cannot add document.")
        return False
    except Exception as e:
        logger.error(f"❌ An unexpected error occurred during the FAISS update process: {e}")
        return False

async def add_to_knowledge_base_async(data: Dict[str, Any]) -> bool:
    """
    Asynchronously adds a new document to the FAISS vector database.

    This function validates input, creates a LangChain Document, and then runs
    the synchronous, blocking file I/O operations in a separate thread to
    keep the main application responsive.

    Args:
        data (Dict[str, Any]): A dictionary containing the data for the new document.
                               Must contain 'question' and 'verse_code' keys.

    Returns:
        bool: True if the document was added successfully, False otherwise.
    """
    if not embeddings:
        logger.error("Cannot add document because embeddings are not initialized.")
        return False

    question = data.get("question")
    verse_code = data.get("verse_code")

    if not question or not verse_code:
        logger.warning("Input data is missing 'question' or 'verse_code'.")
        return False

    # Create the LangChain Document object
    metadata = {
        "file_name": data.get("file_name", ""),
        "explanation": data.get("explanation", ""),
        "code": verse_code
    }
    new_document = Document(page_content=question, metadata=metadata)

    # Get the current running event loop
    loop = asyncio.get_running_loop()

    # Run the synchronous (blocking) save function in a thread pool executor
    success = await loop.run_in_executor(
        None,  # Use the default executor
        _add_to_faiss_sync,
        new_document,
        DB_PATH,
        embeddings
    )

    return success