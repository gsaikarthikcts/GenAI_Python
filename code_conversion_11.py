import requests
 
# Azure OpenAI Configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"

def convert_code(model, from_language, to_language, code):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,  # Use your API key
    }
 
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Convert the following {from_language} code to {to_language}:\n```\n{code}\n```",
            }
        ]
    }
 
    response = requests.post(
        f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
        headers=headers,
        json=data,
    )
 
    response_data = response.json()
    converted_code = response_data["choices"][0]["message"]["content"]
 
    return converted_code










# import requests
# import uuid
 
# # Azure OpenAI Configuration
# api_key = "365aea46115446a48693b001ebd1b74b"
# endpoint = "https://user-story-integration-openai.openai.azure.com/"
# deployment_name = "user-story-deployment-gpt-35"
 
# # Enter the source code
# source_code = input("Enter your code: ")
 
# # Source Code Language (handle potential errors)
# while True:
#     source_code_language = input("Enter your source code language: ").lower()
#     if source_code_language in ("python", "java", "javascript", "cpp", "c#"):
#         break
#     else:
#         print(f"Unsupported source language: {source_code_language}. Please try again.")
 
# # Target Language (handle potential errors)
# while True:
#     target_language = input("Enter target language: ").lower()
#     if target_language in ("python", "java", "javascript", "cpp", "c#"):
#         break
#     else:
#         print(f"Unsupported target language: {target_language}. Please try again.")
 
# if source_code:
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key,  # Corrected key
#     }
 
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": f"Convert the following {source_code_language} code to {target_language}:\n`\n{source_code}\n`",
#             }
#         ]
#     }
 
#     response = requests.post(
#         f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
#         headers=headers,
#         json=data,
#     )
 
#     response_data = response.json()
#     # Extract the converted code from the response
#     converted_code = response_data["choices"][0]["message"]["content"]
 
#     print(f"\nConverted Code:\n`\n{converted_code}\n`")