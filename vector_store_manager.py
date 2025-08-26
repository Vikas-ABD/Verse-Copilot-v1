# ==============================================================================
# File 1: vector_store_manager.py (UPDATED)
# ==============================================================================
# This module now loads and manages BOTH of your FAISS vector stores.

import os
import getpass
import logging
from typing import Dict, Optional
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# --- Configure Logging and Environment ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()
logger.info("Environment variables loaded if .env file exists.")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Configuration for your two RAG databases ---
DB_PATHS = {
    "verse_rag": "faiss_index",          # Path for your Verse code RAG
    "device_rag": "Device_context_db"   # Path for your Device context RAG
}

# --- In-memory cache for the loaded vector stores ---
_vector_stores: Dict[str, FAISS] = {}

# --- Initialize Embeddings Once ---
# This is shared by all vector stores that use it.
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

def load_all_vector_stores():
    """
    Loads all defined FAISS vector stores into memory.
    This function should be called once when the application starts.
    """
    logger.info("Starting to load all vector stores...")
    
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API Key: ")

    for name, path in DB_PATHS.items():
        if not os.path.exists(path):
            logger.warning(f"Database path not found for '{name}' at '{path}'. Skipping.")
            continue
        
        try:
            logger.info(f"Loading vector store for '{name}' from '{path}'...")
            store = FAISS.load_local(
                folder_path=path,
                embeddings=embeddings,
                allow_dangerous_deserialization=True
            )
            _vector_stores[name] = store
            logger.info(f"Successfully loaded vector store for '{name}'.")
        except Exception as e:
            logger.error(f"Failed to load vector store for '{name}' from '{path}': {e}")

def get_vector_store(name: str) -> Optional[FAISS]:
    """
    Retrieves a pre-loaded vector store by its name.
    """
    return _vector_stores.get(name)