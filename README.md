# Aurora-Demo-QA-system

# Member QA Service (LangChain + FastAPI)

This service answers natural-language questions about members by retrieving
and analyzing their messages from the provided API.

## Endpoints

GET /ask?q=Your question

### Example
GET /ask?q=When is Layla planning her trip to London?

Response:
{ "answer": "Layla mentioned she is planning her trip to London on March 25." }

---

## Architecture

- FastAPI for HTTP API
- LangChain for RAG pipeline
- SentenceTransformer embeddings
- FAISS vector store
- Groq LLaMA 3 for reasoning

---

## How It Works

1. Fetches messages from public API (`/messages`)
2. Converts messages into vector embeddings
3. Stores embeddings in FAISS
4. On a question:
   - embeds question
   - retrieves top relevant messages
   - prompts LLM with context
   - extracts answer

---

## Deployment (Cloud Run)

1. Build and push image:
gcloud builds submit --tag gcr.io/PROJECT_ID/member-qa

2. Deploy:
gcloud run deploy member-qa
--image gcr.io/PROJECT_ID/member-qa
--platform managed
--region us-central1
--allow-unauthenticated

---

## Deployment (Render)

1. Create new Web Service
2. Select your GitHub repo
3. Set build command:

pip install -r app/requirements.txt && python app/ingest.py

4. Start command:
uvicorn main:app --host 0.0.0.0 --port 10000

## Notes

This project uses RAG with deterministic retrieval to avoid hallucinations.