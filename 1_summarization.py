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
 
def generate_summary(text, prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt.format(text)}
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
    collection.add(ids=[doc_id],documents=[text],metadatas=[{"summary": summary}])
    return doc_id
 
def handle_user_query(pdf_text, query_type, count=None):
    if query_type == 1:
        prompt = f"Summarize the following text in {count} bullet points: {{}}"
    elif query_type == 2:
        prompt = f"Summarize the following text in {count} sentences: {{}}"
    elif query_type == 3:
        prompt = f"Summarize the following text in detail: {{}}"
    elif query_type == 4:
        prompt = f"Summarize the following text in short: {{}}"
    else:
        return "Invalid option."
    summary = generate_summary(pdf_text, prompt)
    return summary
