
import os
import getpass
import logging
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# --- Configure Logging and Environment ---
# Sets up basic logging to see the script's progress and any potential issues.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Loads environment variables from a .env file if it exists.
load_dotenv()
logger.info("Environment variables loaded if .env file exists.")


# --- Configuration ---
# IMPORTANT: Set this to the path of your folder containing the .md files.
SOURCE_DOCUMENTS_PATH = "Data/Devices"
# Set the path where you want to store the FAISS vector database locally.
PERSIST_DIRECTORY = "./Device_context_db"


def load_markdown_documents(folder_path: str) -> list[Document]:
    """
    Loads all .md files from a specified folder, creating a Document for each.

    For each file:
    - The 'page_content' is derived from the filename (e.g., "player_spawn_device.md"
      becomes "Device Name: player_spawn_device").
    - The 'metadata' contains the full content of the markdown file.

    Args:
        folder_path: The path to the folder containing the .md files.

    Returns:
        A list of LangChain Document objects.
    """
    documents = []
    if not os.path.isdir(folder_path):
        logger.error(f"Source directory '{folder_path}' not found. Please create it and add your .md files.")
        return documents

    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Read the entire content of the file for the metadata
                    content = f.read()

                # Process the filename to create the page_content
                base_name = os.path.splitext(filename)[0]
                keyword = "device"
                keyword_index = base_name.find(keyword)

                if keyword_index != -1:
                    # Extract the name up to and including "device"
                    device_name = base_name[:keyword_index + len(keyword)]
                else:
                    # Fallback if 'device' isn't in the filename, use the whole name
                    device_name = base_name
                    logger.warning(f"Keyword '{keyword}' not found in filename '{filename}'. Using full base name '{device_name}'.")

                # Create the page content in the desired format
                page_content = f"Device Name: {device_name}"

                # Create the LangChain Document
                doc = Document(
                    page_content=page_content,
                    metadata={"info": content}
                )
                documents.append(doc)
                logger.info(f"Successfully loaded and processed '{filename}'")

            except Exception as e:
                logger.error(f"Failed to process file {file_path}: {e}")

    return documents


def ingest_from_folder_faiss():
    """
    Loads markdown documents from a specified folder, creates embeddings,
    and saves them to a local FAISS vector store.
    """
    # --- 1. Set up Google API Key and Embeddings Model ---
    # Will prompt for the key if the environment variable is not set.
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API Key: ")

    print("Initializing Google Generative AI Embeddings with 'models/text-embedding-004'...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    # --- 2. Load Documents from Folder ---
    print(f"\nLoading documents from '{SOURCE_DOCUMENTS_PATH}'...")
    documents = load_markdown_documents(SOURCE_DOCUMENTS_PATH)

    if not documents:
        print("\nNo documents were loaded. Halting the process.")
        print(f"Please ensure your .md files are in the '{SOURCE_DOCUMENTS_PATH}' directory.")
        return

    print(f"-> {len(documents)} documents were successfully loaded.")

    # --- 3. Create and Save the FAISS Vector Store ---
    print(f"\nCreating FAISS index from {len(documents)} documents...")

    # Ensure the target directory exists
    if not os.path.exists(PERSIST_DIRECTORY):
        os.makedirs(PERSIST_DIRECTORY)
        print(f"Created directory: '{PERSIST_DIRECTORY}'")

    # Create the FAISS index from the documents and embeddings
    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    # Save the created index to the specified local path
    vector_store.save_local(folder_path=PERSIST_DIRECTORY)

    print("\n✅ Ingestion complete!")
    print(f"FAISS vector store has been successfully created and saved at '{PERSIST_DIRECTORY}'.")


if __name__ == "__main__":
    ingest_from_folder_faiss()