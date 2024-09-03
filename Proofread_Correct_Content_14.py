import requests
import os
 
# Azure OpenAI Configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"
 
def load_guidelines(folder_path):
    """Load all Markdown guidelines from the specified folder."""
    guidelines = []
    try:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.md'):
                with open(os.path.join(folder_path, file_name), 'r') as file:
                    guidelines.append(file.read().strip())
    except Exception as e:
        print(f"Error loading guidelines: {e}")
    return "\n\n".join(guidelines)
 
def process_text(action, source_text):
    # Load guidelines
    guidelines_folder_path = "guidelines"  # Update this path if needed
    guidelines = load_guidelines(guidelines_folder_path)
 
    if action == "Proof Read":
        return proofread_text(source_text, guidelines)
    elif action == "Proof Read and Translate":
        return proofread_and_translate_text(source_text, guidelines)
    else:
        raise ValueError("Invalid action")
 
def proofread_text(source_text, guidelines):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }
 
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Do not add any additional new content. "
                           f"Correct any grammatical, punctuation, or spelling errors, and improve clarity. "
                           f"Apply the following guidelines to the provided text and make the necessary changes. "
                           f"Text:{source_text}",
            }
        ]
    }
 
    try:
        response = requests.post(
            f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
            headers=headers,
            json=data,
        )
        response.raise_for_status()
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred during the request: {e}")
 
def proofread_and_translate_text(source_text, guidelines):
    # Implement translation and proofreading combined logic if needed
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }
 
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Do not add any additional new content. "
                           f"Correct any grammatical, punctuation, or spelling errors, and improve clarity. "
                           f"Apply the following guidelines to the provided text and make the necessary changes. "
                           f"{guidelines}\n\nText:\n{source_text}",
            }
        ]
    }
 
    try:
        response = requests.post(
            f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
            headers=headers,
            json=data,
        )
        response.raise_for_status()
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred during the request: {e}")