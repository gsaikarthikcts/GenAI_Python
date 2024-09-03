import requests
import re
 
# Azure OpenAI Configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"
 
def comment_code(source_code, model):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }
 
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Provide the following code with inline comments explaining each part:\n\n{source_code}",
            },
        ]
    }
 
    response = requests.post(
        f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
        headers=headers,
        json=data,
    )
 
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
 
    response_data = response.json()
    commented_code = response_data["choices"][0]["message"]["content"]
 
    code_block = re.findall(r"```(.*?)```", commented_code, re.DOTALL)
 
    return code_block[0].strip() if code_block else commented_code.strip()