import os
import logging
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
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

async def get_helper_context(query: str, k: int = 7) -> str:
    """
    Retrieves relevant context using a hybrid search from the PRE-LOADED vector store.
    """
    #logger.info(f"🔍 Performing hybrid search for query: \"{query[:50]}...\"")

    # 1. Get the pre-loaded vector store from the loader
    vector_store = get_vector_store("verse_rag")
    if not vector_store:
        return "RAG database is not loaded. Please check application startup logs."

    # 2. Extract documents for the BM25 retriever
    documents = list(vector_store.docstore._dict.values())
    if not documents:
        return "No documents found in the RAG database."

    # 3. Initialize retrievers (this part is fast)
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k
    faiss_retriever = vector_store.as_retriever(search_kwargs={"k": k})
    
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, faiss_retriever], weights=[0.5, 0.5]
    )

    # 4. Asynchronously invoke the search
    retrieved_docs = await ensemble_retriever.ainvoke(query)
    if not retrieved_docs:
        return "No relevant context found in the database."

    # 5. Format the context string
    helper_context = "--- Helper Context ---\n\n"
    for i, doc in enumerate(retrieved_docs):
        helper_context += (
            f"--- Result {i+1} ---\n"
            f"Matched Question: {doc.page_content}\n"
            f"Verse Code:\n```verse\n{doc.metadata['code']}\n```\n\n"
        )
    return helper_context




async def get_helper_context_updated(query: str, k: int = 7) -> str:
    """
    Retrieves relevant context using a hybrid search (BM25 + FAISS) from the
    pre-loaded vector store and formats it as Questions, Code, and Explanation.
    """
    #logger.info(f"🔍 Performing hybrid search for query: \"{query[:50]}...\"")

    # 1. Get the pre-loaded vector store
    # This assumes get_vector_store() loads the FAISS index you created with the new script.
    vector_store = get_vector_store("verse_rag")
    if not vector_store:
        logger.error("RAG database is not loaded. Check application startup.")
        return "RAG database is not loaded. Please check application startup logs."

    # 2. Extract documents for the BM25 retriever
    # This correctly gets all documents from the FAISS docstore.
    documents = list(vector_store.docstore._dict.values())
    if not documents:
        logger.warning("No documents found in the RAG database.")
        return "No documents found in the RAG database."

    # 3. Initialize the hybrid retriever
    # This setup combines keyword-based search (BM25) and semantic search (FAISS).
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k
    
    faiss_retriever = vector_store.as_retriever(search_kwargs={"k": k})
    
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, faiss_retriever], 
        weights=[0.5, 0.5]  # Giving equal importance to both keyword and semantic search
    )

    # 4. Asynchronously perform the search
    retrieved_docs = await ensemble_retriever.ainvoke(query)
    if not retrieved_docs:
        #logger.info(f"No relevant context found for query: \"{query[:50]}...\"")
        return "No relevant context found in the database."

    # 5. Format the context string with the new structure (Questions -> Code -> Explanation)
    #logger.info(f"✅ Found {len(retrieved_docs)} relevant documents. Formatting context.")
    helper_context = "--- Helper Context ---\n\n"
    for i, doc in enumerate(retrieved_docs):
        # Safely get metadata attributes with fallbacks
        code = doc.metadata.get('code', '# Code not available')
        explanation = doc.metadata.get('explanation', 'Explanation not available.')

        helper_context += (
            f"--- Result {i+1} ---\n"
            f"**Questions:**\n{doc.page_content}\n\n"
            f"**Verse Code:**\n```verse\n{code}\n```\n\n"
            f"**Explanation:**\n{explanation}\n\n"
        )
        
    return helper_context