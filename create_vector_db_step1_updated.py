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
# Directory containing your JSON files, potentially in subfolders
DATA_FOLDER_PATH = "Data/Projects"
DB_PATH = "faiss_index"
FORCE_RECREATE = True # Set to True to overwrite existing database

# --- Initialize Embeddings ---
    
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

def load_documents_from_folder(folder_path: str) -> list[Document]:
    """
    Walks through a directory, finds all .json files, and loads them
    into a list of LangChain Document objects.
    
    This function handles .json files containing either a single JSON object
    or a list of JSON objects.
    """
    print(f"📂 Searching for JSON files in '{folder_path}'...")
    json_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    if not json_files:
        print(f"⚠️ Warning: No JSON files found in '{folder_path}'.")
        return []

    print(f"✅ Found {len(json_files)} JSON files to process.")
    
    loaded_documents = []
    skipped_files_count = 0
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            records_to_process = []
            if isinstance(data, dict):
                # If it's a single object, wrap it in a list to standardize processing
                records_to_process = [data]
            elif isinstance(data, list):
                # If it's already a list, use it directly
                records_to_process = data
            else:
                print(f"⚠️ Warning: Skipping '{file_path}' because its content is not a JSON object or a list of objects.")
                skipped_files_count += 1
                continue

            for record in records_to_process:
                # Ensure each item in the list is a dictionary before processing
                if not isinstance(record, dict):
                    print(f"⚠️ Warning: Skipping a non-dictionary item within '{file_path}'.")
                    continue

                # Join all questions into a single string for page_content
                questions = " ".join(record.get("questions", []))
                
                # If there are no questions, there's nothing to embed. Skip this record.
                if not questions:
                    print(f"⚠️ Warning: Skipping a record in '{file_path}' because it has no 'questions'.")
                    continue
                    
                # Store the other fields in metadata
                metadata = {
                    "file_name": record.get("file_name", os.path.basename(file_path)),
                    "explanation": record.get("explanation", ""),
                    "code": record.get("code", "")
                }
                
                # Create the LangChain Document
                doc = Document(page_content=questions, metadata=metadata)
                loaded_documents.append(doc)

        except json.JSONDecodeError as e:
            print(f"❌ Error decoding JSON from '{file_path}': {e}. Skipping.")
            skipped_files_count += 1
        except Exception as e:
            print(f"❌ An unexpected error occurred with file '{file_path}': {e}. Skipping.")
            skipped_files_count += 1
            
    if skipped_files_count > 0:
        print(f"ℹ️ Skipped a total of {skipped_files_count} files (or parts of files) due to errors or missing data.")
        
    return loaded_documents


def create_custom_documents() -> list[Document]:
    """
    Creates and returns a list of custom, hard-coded Document objects.
    This is the space where you can add your own data manually.
    """
    print("✍️ Adding custom documents...")
    custom_docs = [
        Document(
            page_content="How do I create a timer in Verse? What's the code for a countdown?",
            metadata={
                "file_name": "custom_timer.verse",
                "explanation": "This is a custom document demonstrating a simple countdown timer. It uses a loop with a sleep function to wait for one-second intervals and updates a variable accordingly. Ideal for basic gameplay mechanics.",
                "code": """
my_timer := class():
    RunTimer(Seconds: int):void=
        for(i := 0..Seconds):
            Print("Time remaining: {Seconds - i}")
            Sleep(1.0)
        Print("Time's up!")
"""
            }
        ),
        # You can add more Document objects here
        # Document(page_content="...", metadata={...}),
    ]
    print(f"✅ Added {len(custom_docs)} custom documents.")
    return custom_docs

def populate_vector_db(data_folder_path: str, db_path: str, force_recreate: bool = False):
    """
    Loads documents from a folder and custom sources, then populates a FAISS
    vector store.
    """
    if os.path.exists(db_path) and not force_recreate:
        print(f"✅ FAISS database already exists at '{db_path}'. Skipping population.")
        return

    # 1. Load documents from the JSON files in the specified folder
    documents_from_files = load_documents_from_folder(data_folder_path)

    # 2. Create and add your custom documents
    custom_docs = create_custom_documents()
    
    # 3. Combine all documents into one list
    all_documents = documents_from_files + custom_docs

    if not all_documents:
        print("❌ No valid documents were loaded or created. Cannot create the database. Exiting.")
        return

    # 4. Populate the FAISS index with the combined documents
    print(f"\n⏳ Populating FAISS vector database from a total of {len(all_documents)} documents...")
    print("🧠 Creating FAISS index from documents...")
    try:
        vector_store = FAISS.from_documents(
            documents=all_documents,
            embedding=embeddings
        )
        print(f"💾 Saving FAISS index to '{db_path}'...")
        vector_store.save_local(db_path)
        print(f"✅ FAISS database population complete. Index saved at '{db_path}'.")

    except Exception as e:
        print(f"❌ An error occurred during FAISS index creation: {e}")
        print("   Please ensure your GOOGLE_API_KEY is correctly set in your environment.")


if __name__ == "__main__":
    # Create the 'Data' directory if it doesn't exist to avoid errors
    if not os.path.exists(DATA_FOLDER_PATH):
        os.makedirs(DATA_FOLDER_PATH)
        print(f"📁 Created '{DATA_FOLDER_PATH}' directory. Please add your JSON files to this folder.")
    
    # Run the main function to populate the database
    populate_vector_db(DATA_FOLDER_PATH, DB_PATH, FORCE_RECREATE)