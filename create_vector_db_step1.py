import json
import os
import logging
from langchain.schema.document import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

# --- Configure Logging and Environment ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
load_dotenv()
logger.info("Environment variables loaded if .env file exists.")

# --- Configuration ---
# Make sure your JSONL file is placed in the 'Data' folder
JSONL_FILE_PATH = os.path.join("Data", "updated_Training_Data_10-05-25.jsonl") # Replace with your JSONL file name
DB_PATH = "faiss_index"
FORCE_RECREATE = True # Set to True to overwrite existing database

# --- Initialize Embeddings ---
# Make sure you have your Google API key set up in your environment
# For example, os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

def populate_vector_db_from_jsonl(jsonl_file_path: str, db_path: str, force_recreate: bool = False):
    """
    Loads data from a JSONL file with a specific "contents" structure,
    populates the FAISS vector store if needed, and returns the loaded documents.
    """
    print(f"⏳ Loading documents from {jsonl_file_path}...")

    if not os.path.exists(jsonl_file_path):
        print(f"❌ Error: The file was not found at {jsonl_file_path}")
        return None

    # Skip populating if the database already exists and force_recreate is False
    if os.path.exists(db_path) and not force_recreate:
        print(f"✅ FAISS database already exists at {db_path}. Skipping population.")
        return

    verse_data = []
    skipped_lines_count = 0
    try:
        with open(jsonl_file_path, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, 1):
                try:
                    data = json.loads(line)
                    # The question is in the 'user' role part
                    question = data['contents'][0]['parts'][0]['text']
                    # The code is in the 'model' role part
                    code = data['contents'][1]['parts'][0]['text']
                    verse_data.append({"question": question, "code": code})
                except (json.JSONDecodeError, KeyError, IndexError) as e:
                    print(f"⚠️ Warning: Skipping malformed line #{line_number}. Error: {e}")
                    skipped_lines_count += 1
                    continue
    except FileNotFoundError:
        print(f"❌ Error: The file was not found at {jsonl_file_path}")
        return None

    # Create LangChain Document objects
    documents = [
        Document(page_content=entry["question"], metadata={"code": entry["code"]})
        for entry in verse_data
    ]

    if skipped_lines_count > 0:
        print(f"ℹ️ Skipped a total of {skipped_lines_count} malformed lines.")

    if not documents:
        print("❌ No valid documents were loaded. Cannot create the database. Exiting.")
        return

    # Populate FAISS index
    print(f"⏳ Populating FAISS vector database from {len(documents)} documents...")
    print("🧠 Creating FAISS index from documents...")
    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )
    print(f"💾 Saving FAISS index to {db_path}...")
    vector_store.save_local(db_path)
    print(f"✅ FAISS database population complete. Index saved at '{db_path}'.")

if __name__ == "__main__":
    # Create the 'Data' directory if it doesn't exist
    if not os.path.exists("Data"):
        os.makedirs("Data")
        print("📁 Created 'Data' directory. Please add your JSONL file to this folder.")
    else:
        # Run the main function to populate the database
        populate_vector_db_from_jsonl(JSONL_FILE_PATH, DB_PATH, FORCE_RECREATE)
