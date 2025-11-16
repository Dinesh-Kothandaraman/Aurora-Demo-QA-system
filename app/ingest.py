import requests
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from .config import API_URL, EMBED_MODEL
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("Swagger_api_key")

def load_messages():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json"
    }

    res = requests.get(API_URL, headers=headers)
    res.raise_for_status()
    data = res.json()

    documents = []
    for m in data.get("items", []):
        documents.append(Document(page_content=m["message"], metadata={}))

    return documents


def create_vectorstore():
    docs = load_messages()
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectorstore = FAISS.from_documents(docs, embedder)
    vectorstore.save_local("faiss_store")

if __name__ == "__main__":
    create_vectorstore()
    print("Vectorstore created!")
