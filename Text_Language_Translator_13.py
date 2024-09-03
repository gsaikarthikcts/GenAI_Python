import requests
import langdetect
 
# Azure OpenAI Configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"
 
def perform_translation(model, source_lang, target_lang, text):
    # Detect language (optional)
    detected_language = langdetect.detect(text)
    # Handle translation based on selected model
    if model == "Azure OpenAI":
        headers = {
            "Content-Type": "application/json",
            "api-key": api_key,
        }
 
        data = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Translate the following text: {text} \n from {source_lang} to {target_lang}",
                }
            ]
        }
 
        response = requests.post(
            f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
            headers=headers,
            json=data,
        )
        response_data = response.json()
        translated_text = response_data["choices"][0]["message"]["content"]
    # Add logic for other models (e.g., Google Palm, Llama2) if necessary
    return translated_text











# import requests
# import langdetect
 
# # Azure OpenAI Configuration
# api_key = "365aea46115446a48693b001ebd1b74b"
# endpoint = "https://user-story-integration-openai.openai.azure.com/"
# deployment_name = "user-story-deployment-gpt-35"
 
# # Enter the text_data
# text_data = input("Enter your text: ")
 
# #Detect Language
# detected_language = langdetect.detect_langs(text_data)[0].lang
# # Target Language
# target_language = input("Enter target language: ").lower()
 
# if text_data:
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key,  
#     }
 
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": f" Translate the following text: {text_data} \n from {detected_language} language to:\n`\n{target_language}\n`",
#             }
#         ]
#     }
 
#     response = requests.post(
#         f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
#         headers=headers,
#         json=data,
#     )
 
#     response_data = response.json()
#     # Extract the translated text from the response
#     translated_text = response_data["choices"][0]["message"]["content"]
 
#     print(f"\n Translated Text :\n`\n{translated_text}\n`")