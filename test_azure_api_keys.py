import requests
 
# Set the endpoint and API key
endpoint = "https://user-story-integration-openai.openai.azure.com/"
api_key = "365aea46115446a48693b001ebd1b74b"
 
# Define a test function
def test_api_key():
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
 
    test_url = f"{endpoint}/openai/deployments?api-version=2022-12-01"
 
    try:
        response = requests.get(test_url, headers=headers)
        response.raise_for_status()
        print("API Key is working. Response:Done")
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
 
# Call the test function
if __name__ == "__main__":
    test_api_key()