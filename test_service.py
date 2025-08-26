# import requests
# import json

# # The base URL of your running FastAPI application
# BASE_URL = "http://localhost:8000"

# def test_add_knowledge_live_success():
#     """
#     Sends a real HTTP POST request to a running server with valid data.
#     """
#     print("\n--- Running test_add_knowledge_live_success ---")
    
#     # The endpoint we are testing
#     url = f"{BASE_URL}/add-knowledge1"
    
#     # Sample valid payload
#     payload = {
#         "question": "How can I check the distance between two players in Verse?",
#         "verse_code": """
# Distance(Agent1:agent, Agent2:agent):float=
#     if (FortChar1 := Agent1.GetFortCharacter[], FortChar2 := Agent2.GetFortCharacter[]):
#         return Distance(FortChar1.GetTransform().Translation, FortChar2.GetTransform().Translation)
#     return 0.0
# """
#     }
    
#     try:
#         # Send the request
#         response = requests.post(url, json=payload)
        
#         # Check if the request was successful
#         response.raise_for_status()  # This will raise an exception for 4xx or 5xx status codes

#         # Assert the response content
#         response_data = response.json()
#         assert response.status_code == 200 # Or 201, depending on your API's success code
#         assert response_data.get("status") == "success"
        
#         print(f"✅ SUCCESS: API responded with status {response.status_code} and success message.")
        
#     except requests.exceptions.RequestException as e:
#         print(f"❌ FAILED: Could not connect to the server or request failed. Is the server running at {BASE_URL}?")
#         print(f"   Error: {e}")
#         assert False, "Test failed due to a request exception."


# def test_add_knowledge_live_failure_validation():
#     """
#     Sends a real HTTP POST request with invalid data to check validation.
#     """
#     print("\n--- Running test_add_knowledge_live_failure_validation ---")
    
#     url = f"{BASE_URL}/add-knowledge1"
    
#     # Invalid payload (missing 'question')
#     invalid_payload = {
#         "verse_code": "var X: int = 5"
#     }
    
#     try:
#         response = requests.post(url, json=invalid_payload)
        
#         # For this test, we expect a client error (4xx)
#         assert 400 <= response.status_code < 500
#         # Specifically, FastAPI's validation error is 422
#         assert response.status_code == 422
        
#         response_data = response.json()
#         assert "detail" in response_data
        
#         print(f"✅ SUCCESS: API correctly returned a validation error with status code {response.status_code}.")
        
#     except requests.exceptions.RequestException as e:
#         print(f"❌ FAILED: Could not connect to the server. Is it running at {BASE_URL}?")
#         print(f"   Error: {e}")
#         assert False, "Test failed due to a request exception."

# if __name__ == "__main__":
#     # This allows you to run the file directly like a normal Python script
#     test_add_knowledge_live_success()
#     test_add_knowledge_live_failure_validation()




import requests
import json
import os

# The base URL of your running FastAPI application
# It's good practice to allow overriding via environment variables for CI/CD
BASE_URL = os.getenv("TEST_BASE_URL", "http://127.0.0.1:8000")

def test_summarize_youtube_success():
    """
    Sends a real HTTP POST request to a running server with a valid YouTube URL.
    This test will make a live call to the Gemini API, so it may take a few seconds.
    """
    print("\n--- Running test_summarize_youtube_success ---")
    
    # The endpoint we are testing
    url = f"{BASE_URL}/summarize-youtube-video"
    
    # A valid, public YouTube URL to test with
    # Using a short, well-known video is ideal.
    payload = {
        "youtube_url": "https://www.youtube.com/watch?v=UrRBuqt0lmg"
    }
    
    print(f"Submitting request to {url} with URL: {payload['youtube_url']}")
    
    try:
        # Send the request
        response = requests.post(url, json=payload, timeout=60) # Increased timeout for AI processing
        
        # This will raise an exception for 4xx or 5xx status codes
        response.raise_for_status()

        # Assert the response content
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get("status") == "success"
        assert "summary" in response_data
        assert len(response_data["summary"]) > 10 # Check that the summary is not empty
        
        print(f"✅ SUCCESS: API responded with status {response.status_code} and a valid summary.")
        print(f"   Summary received: {response_data['summary']}...") # Optional: print snippet
        
    except requests.exceptions.RequestException as e:
        print(f"❌ FAILED: Could not connect or the request timed out. Is the server running at {BASE_URL}?")
        print(f"   Error: {e}")
        assert False, "Test failed due to a request exception."


def test_summarize_youtube_failure_validation():
    """
    Sends a real HTTP POST request with an invalid payload to check validation.
    This should fail fast without calling the Gemini API.
    """
    print("\n--- Running test_summarize_youtube_failure_validation ---")
    
    url = f"{BASE_URL}/summarize-youtube-video"
    
    # Invalid payload (e.g., wrong key name 'url' instead of 'youtube_url')
    invalid_payload = {
        "url": "https://www.youtube.com/watch?v=UrRBuqt0lmg"
    }
    
    try:
        response = requests.post(url, json=invalid_payload, timeout=10)
        
        # We expect a client error (4xx) due to invalid input
        # FastAPI's Pydantic validation error code is 422 Unprocessable Entity
        assert response.status_code == 422
        
        response_data = response.json()
        assert "detail" in response_data
        
        print(f"✅ SUCCESS: API correctly returned a validation error with status code {response.status_code}.")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ FAILED: Could not connect to the server. Is it running at {BASE_URL}?")
        print(f"   Error: {e}")
        assert False, "Test failed due to a request exception."

def test_summarize_youtube_failure_invalid_url():
    """
    Sends a real request with a syntactically valid but non-existent YouTube URL.
    This tests the server's ability to handle errors from the Gemini API.
    """
    print("\n--- Running test_summarize_youtube_failure_invalid_url ---")

    url = f"{BASE_URL}/summarize-youtube-video"

    # Payload with a URL that will likely cause an error in the backend service
    payload = {
        "youtube_url": "https://www.youtube.com/watch?v=UrRBuqt0lm"
    }

    print(f"Submitting request to {url} with intentionally invalid URL: {payload['youtube_url']}")

    try:
        response = requests.post(url, json=payload, timeout=30)
        
        # We expect a server-side error because the summarization service should fail
        assert response.status_code == 500
        
        response_data = response.json()
        assert "detail" in response_data
        
        print(f"✅ SUCCESS: API correctly handled a backend error and returned status {response.status_code}.")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ FAILED: Could not connect to the server. Is it running at {BASE_URL}?")
        print(f"   Error: {e}")
        assert False, "Test failed due to a request exception."


if __name__ == "__main__":
    print("--- Starting Live API Tests for YouTube Summarizer ---")
    print(f"--- Target Server: {BASE_URL} ---")
    print("NOTE: Ensure your FastAPI server is running before executing these tests.")
    
    test_summarize_youtube_success()
    test_summarize_youtube_failure_validation()
    test_summarize_youtube_failure_invalid_url()
    
    print("\n--- All tests completed. ---")