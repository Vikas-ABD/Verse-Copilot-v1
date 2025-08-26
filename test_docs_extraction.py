# import asyncio
# from bs4 import BeautifulSoup
# from langchain_community.document_loaders import PlaywrightURLLoader

# # The URL for the Scene Graph documentation
# urls = [
#     "https://dev.epicgames.com/documentation/en-us/fortnite/scene-graph-in-unreal-editor-for-fortnite"
# ]

# print(f"Starting JavaScript-enabled scrape for: {urls[0]}")

# # This custom function extracts text from the specific content area of the site
# def epic_dev_portal_extractor(html: str) -> str:
#     """
#     Based on the site's structure, the main content is inside the <main> tag.
#     This function specifically targets that tag to get clean text.
#     """
#     soup = BeautifulSoup(html, "lxml")
#     # From your images, the main content is within a <main> tag
#     main_content = soup.find("main")
#     if main_content:
#         return main_content.get_text(separator='\n', strip=True)
#     return "" # Return empty if the main tag isn't found

# # The main asynchronous function to run the loader
# async def main():
#     # Instantiate the PlaywrightURLLoader
#     # It will load the URLs in a headless browser, running all JavaScript
#     loader = PlaywrightURLLoader(urls=urls, remove_selectors=["header", "footer"])
    
#     print("Loading page in headless browser...")
#     docs = await loader.aload()
    
#     # Process the loaded documents with our custom extractor
#     final_docs = []
#     for doc in docs:
#         extracted_text = epic_dev_portal_extractor(doc.page_content)
#         # Create a new document with the clean, extracted text
#         # You can also just process the text directly if you prefer
#         from langchain_core.documents import Document
#         new_doc = Document(
#             page_content=extracted_text,
#             metadata=doc.metadata
#         )
#         final_docs.append(new_doc)

#     print("\n--- Scraping Complete! ---")
#     print(f"Successfully scraped and processed {len(final_docs)} page(s).")
    
#     if final_docs:
#         print("\n--- Example content from the scraped page ---")
#         # Print the first 700 characters of the clean content
#         print(final_docs[0].page_content[:700] + "...")
#         print(f"\nSource URL: {final_docs[0].metadata['source']}")

# # Run the asynchronous main function
# if __name__ == "__main__":
#     asyncio.run(main())