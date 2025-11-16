from fastapi import FastAPI
from chains import qa_chain

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    answer = qa_chain(q)
    return {"answer": answer}
