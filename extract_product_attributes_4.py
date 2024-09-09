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
                    "content": f"Provide product details for: {product_name}. Only output any 6 main Attributes",
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

