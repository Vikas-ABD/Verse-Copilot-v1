import os 
import logging
# Import the manager to get the pre-loaded store
from vector_store_manager import  get_vector_store
from dotenv import load_dotenv

# Load environment variables at the earliest possible moment
load_dotenv()

# Explicitly get the API key from the environment
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    # This will make the app crash immediately if the key is missing, which is good for debugging.
    raise ValueError("GOOGLE_API_KEY environment variable not found.")



logger = logging.getLogger(__name__)

# --- Main Asynchronous Query Function ---
# --- Device RAG Function (Refactored from your code) ---
async def get_device_context(user_query: str, k: int) -> str:
    """
    Asynchronously queries the pre-loaded 'device_rag' FAISS DB for the top k devices.
    """
    # 1. Get the pre-loaded vector store. No more loading from disk here!
    vector_store = get_vector_store("device_rag")
    if not vector_store:
        return "Device RAG vector store could not be initialized. Check startup logs."

    if not isinstance(k, int) or k <= 0:
        return "Error: k must be a positive integer."

    #logger.info(f"Performing async FAISS search for query: '{user_query}' with k={k}...")
    
    # 2. Perform the asynchronous similarity search.
    try:
        results = await vector_store.asimilarity_search(query=user_query, k=k)
    except Exception as e:
        return f"An error occurred during the search: {e}"

    if not results:
        return f"No results found for the query: '{user_query}'"

    # 3. Format the results into a single string.
    all_info = []
    for doc in results:
        device_name = doc.page_content.replace("Device Name:", "").strip()
        info_string = doc.metadata.get('info', 'No information available.')
        all_info.append(f"Device: {device_name}\nInfo: {info_string}\n")

    return "\n---\n".join(all_info)
