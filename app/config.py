import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://november7-730026606190.europe-west1.run.app/messages"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
