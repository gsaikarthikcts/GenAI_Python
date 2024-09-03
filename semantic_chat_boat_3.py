import requests
import chromadb
from PyPDF2 import PdfReader
import uuid
 
# Azure OpenAI configuration
api_key = "365aea46115446a48693b001ebd1b74b"
endpoint = "https://user-story-integration-openai.openai.azure.com/"
deployment_name = "user-story-deployment-gpt-35"
 
# Configure Chroma
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="pdf_summaries")

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_summary(text):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text: {text}"}
        ]
    }

    response = requests.post(
        f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
        headers=headers,
        json=data
    )

    response_data = response.json()
    return response_data['choices'][0]['message']['content']

def store_summary_in_chroma(text, summary):
    doc_id = str(uuid.uuid4())
    collection.add(
        ids=[doc_id],
        documents=[text],
        metadatas=[{"summary": summary}]
    )
 
def answer_question(question):
    results = collection.get()
    summaries = [meta['summary'] for meta in results['metadatas']]
    combined_summaries = ' '.join(summaries)
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following summaries: {combined_summaries}, answer the following question: {question}"}
        ]
    }

    response = requests.post(
        f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
        headers=headers,
        json=data
    )

    response_data = response.json()
    return response_data['choices'][0]['message']['content']
 



# import requests
# import chromadb
# from PyPDF2 import PdfReader
# import uuid

# # Azure OpenAI configuration
# api_key = "365aea46115446a48693b001ebd1b74b"
# endpoint = "https://user-story-integration-openai.openai.azure.com/"
# deployment_name = "user-story-deployment-gpt-35"

# # Configure Chroma
# chroma_client = chromadb.Client()
# collection = chroma_client.get_or_create_collection(name="pdf_summaries")

# def extract_text_from_pdf(pdf_path):
#     reader = PdfReader(pdf_path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# def generate_summary(text):
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key
#     }
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"Summarize the following text: {text}"}
#         ]
#     }
#     response = requests.post(
#         f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
#         headers=headers,
#         json=data
#     )
#     response_data = response.json()
#     return response_data['choices'][0]['message']['content']

# def store_summary_in_chroma(text, summary):
#     doc_id = str(uuid.uuid4())
#     collection.add(
#         ids=[doc_id],
#         documents=[text],
#         metadatas=[{"summary": summary}]
#     )

# def answer_question(question):
#     results = collection.get()
#     summaries = [meta['summary'] for meta in results['metadatas']]
#     combined_summaries = ' '.join(summaries)

#     headers = {
#         "Content-Type": "application/json",
#         "api-key": api_key
#     }
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"Based on the following summaries: {combined_summaries}, answer the following question: {question}"}
#         ]
#     }
#     response = requests.post(
#         f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2023-03-15-preview",
#         headers=headers,
#         json=data
#     )
#     response_data = response.json()
#     return response_data['choices'][0]['message']['content']

# def chatbot():
#     print("Chatbot: Hello! I'm here to help you with your PDF documents.")
    
#     # Step 1: Upload and Process PDF
#     pdf_path = input("Chatbot: Please enter the path to your PDF file: ")
#     print("Chatbot: Processing your PDF...")
#     pdf_text = extract_text_from_pdf(pdf_path)
#     summary = generate_summary(pdf_text)
#     store_summary_in_chroma(pdf_text, summary)
#     print("Chatbot: I've summarized your PDF and stored it. You can now ask me questions about its content.")

#     # Step 2: Interactive Chat
#     while True:
#         user_input = input("\nYou: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Chatbot: Goodbye! If you need anything else, just ask.")
#             break
        
#         answer = answer_question(user_input)
#         print(f"Chatbot: {answer}")

# if __name__ == "__main__":
#     chatbot()
