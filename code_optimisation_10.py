import requests
import re
 
# Azure OpenAI Configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"
 
def optimize_code(source_code, model):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }
 
    # Data payload for the Azure OpenAI API request
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Optimize the following code for performance and maintainability:\n{source_code}.",
            },
        ]
    }
 
    # Make a request to the Azure OpenAI API
    response = requests.post(
        f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
        headers=headers,
        json=data,
    )
 
    # Parse the response
    response_data = response.json()
    optimized_code = response_data["choices"][0]["message"]["content"]
 
    # Use regex to extract just the code block from the response
    # The code block is usually enclosed in triple backticks or similar formatting
    code_block = re.findall(r"```(.*?)```", optimized_code, re.DOTALL)
 
    # If a code block is found, return it; otherwise, return the entire message
    return code_block[0].strip() if code_block else optimized_code.strip()








# import requests
 
# # Azure OpenAI Configuration
# api_key = "365aea46115446a48693b001ebd1b74b"
# endpoint = "https://user-story-integration-openai.openai.azure.com/"
# deployment_name = "user-story-deployment-gpt-35"
 
# # Enter the source code
# source_code = input("Enter your code: ")
 
# if source_code:
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key,
#     }

#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": f"Optimize the following code:{source_code} for performance and maintainability .Additionally, provide an updated version of the code with the changes made.",
               
#             }
#         ]
#     }
 
#     response = requests.post(
#         f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
#         headers=headers,
#         json=data,
#     )
 
#     response_data = response.json()
#     # Extract the optimized code from the response
#     optimized_code = response_data["choices"][0]["message"]["content"]
 
#     print(f"\nOptimized  Code:\n`\n{optimized_code}\n`")