import requests
 
# Azure OpenAI Configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"
 
def get_product_details(product_name, model):
    if model == "azure":
        headers = {
            "Content-Type": "application/json",
            "api-key": api_key,
        }
        body = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Provide product details for: {product_name}. Only output model name, storage, camera, battery, price, and processor.",
                }
            ]
        }
 
        response = requests.post(
            f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
            headers=headers,
            json=body,
        )
 
        response_data = response.json()
        product_details = response_data["choices"][0]["message"]["content"]
 
        return product_details
 
    # Extend this function to handle other models
    return "Product details extraction not supported for this model."















# import requests
 
# # Azure OpenAI Configuration
# api_key = "365aea46115446a48693b001ebd1b74b"
# endpoint = "https://user-story-integration-openai.openai.azure.com/"
# deployment_name = "user-story-deployment-gpt-35"
 
# # Enter the source code
# product_name = input("Enter Product Name: ")
 
# if product_name:
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key,
#     }
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": f" Provide specify product details for:{product_name} .Only give output of model name ,storage ,camera, battery , price and processor.",          
#             }
#         ]
#     }
 
#     response = requests.post(
#         f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
#         headers=headers,
#         json=data,
#     )
 
#     response_data = response.json()
#     # Extract the Product Details from the response
#     product_details = response_data["choices"][0]["message"]["content"]
#     print(f"\n Product Details:\n`\n{product_details}\n`")