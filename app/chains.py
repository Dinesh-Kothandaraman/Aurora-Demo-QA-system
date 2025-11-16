from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import EMBED_MODEL, GROQ_API_KEY, LLM_MODEL

# Load FAISS store
embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
faiss_store = FAISS.load_local("faiss_store", embedder, allow_dangerous_deserialization=True)

# Convert FAISS store into a retriever
retriever = faiss_store.as_retriever(search_kwargs={"k": 5})

# Prompt template
prompt = PromptTemplate(
    template="""
Use ONLY the information from these messages to answer the question.
If the answer is not present, say "Not mentioned".

Messages:
{context}

Question: {question}

Answer:
""",
    input_variables=["context", "question"]
)

# Initialize LLM
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model=LLM_MODEL)

# QA function
def qa_chain(question: str):
    # New way: use .invoke()
    docs = retriever.invoke(question)          # ← this is the correct method now
    
    # Combine text
    context = "\n".join([d.page_content for d in docs])
    
    # Query the LLM
    answer = llm.invoke(prompt.format(context=context, question=question))
    return answer.content
