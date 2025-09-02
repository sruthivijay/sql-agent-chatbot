from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI, OpenAIEmbeddings,AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Union, Literal
#from langchain_postgres import PGEngine, PGVectorStore
# Embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# Vector stores
from langchain_community.vectorstores import FAISS, Qdrant,PGVector

import os
from dotenv import load_dotenv

load_dotenv()

# =============== CONFIG ===================
OPENAI_API_KEY = "76c80c95dfef4d0692318e5b6f7127f2"
CONNECTION_STRING = "sqlite:///Chinook.db"   # Chinook sample db
PGVECTOR_CONN = "postgresql+psycopg2://user:password@localhost:5432/mydb"

# =============== FASTAPI APP ===============
app = FastAPI()

# =============== LLM =======================
llm = AzureChatOpenAI(
    azure_deployment="gpt-4o",
    temperature=0,
    api_key="76c80c95dfef4d0692318e5b6f7127f2",
    azure_endpoint="https://jpecoai570aoa01.openai.azure.com/",
    api_version="2024-12-01-preview"
)

embeddings = AzureOpenAIEmbeddings(
    azure_deployment="text-embedding-ada-002",
    api_key="76c80c95dfef4d0692318e5b6f7127f2",
    azure_endpoint="https://jpecoai570aoa01.openai.azure.com/",
    api_version="2024-12-01-preview"
)

# =============== SQL AGENT =================
db = SQLDatabase.from_uri(CONNECTION_STRING)
sql_agent = create_sql_agent(llm=llm, db=db, verbose=True)

# =============== PGVECTOR: Dummy Products ===
# Step 1: create schema (run once in Postgres manually)
# CREATE EXTENSION IF NOT EXISTS vector;
# CREATE TABLE IF NOT EXISTS products (id serial primary key, name text, description text, embedding vector(1536));

dummy_products = [
    {"name": "Smart Home Security Camera", "description": "Wireless indoor/outdoor camera with motion detection"},
    {"name": "Solar Inverter", "description": "5kW solar inverter with smart monitoring"},
    {"name": "Energy Efficient LED Bulb", "description": "10W LED bulb with 25,000 hours lifespan"},
]

# product_store = PGVector(
#     connection_string=PGVECTOR_CONN,
#     embedding_function=embeddings,
#     collection_name="products",
# )

# insert dummy product docs (only once)
# def seed_products():
#     docs = [f"{p['name']}: {p['description']}" for p in dummy_products]
#     product_store.add_texts(docs)

# =============== WEBSITE SCRAPER ============
def scrape_website(
    urls: Union[str, List[str]],
    *,
    backend: Literal["qdrant", "faiss"] = "faiss",
    persist_dir: str = "./vector_store",
    collection_name: str = "web",
    chunk_size: int = 1000,
    chunk_overlap: int = 200
):
    """
    Scrape one or more URLs and index content into Chroma or FAISS.

    Args:
        urls: A URL or list of URLs to scrape.
        backend: "chroma" or "faiss".
        persist_dir: Directory to persist the vector store (folder will be created).
        collection_name: Chroma collection name (ignored for FAISS).
        chunk_size: Character chunk size for splitting.
        chunk_overlap: Overlap between chunks.
        embedding_backend: "openai" or "huggingface".
        hf_model_name: HF model name if using HuggingFace embeddings.
        openai_embedding_model: OpenAI embedding model name.

    Returns:
        The created vector store instance and the number of chunks indexed.
    """
    if isinstance(urls, str):
        urls = [urls]

    # 1) Load pages
    docs = []
    for url in urls:
        loader = WebBaseLoader(url)
        docs.extend(loader.load())

    # 2) Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(docs)

    # 3) Choose embeddings
    # if embedding_backend == "openai":
    #     embeddings = AzureOpenAIEmbeddings(model=openai_embedding_model)
    # elif embedding_backend == "huggingface":
    #     embeddings = HuggingFaceEmbeddings(model_name=hf_model_name)
    # else:
    #     raise ValueError("embedding_backend must be 'openai' or 'huggingface'")

    # 4) Build and persist vector store
    if backend == "chroma":
        vs = Qdrant.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=persist_dir,
            collection_name=collection_name,
        )
        vs.persist()
    elif backend == "faiss":
        vs = FAISS.from_documents(chunks, embeddings)
        vs.save_local(persist_dir)
    else:
        raise ValueError("backend must be 'chroma' or 'faiss'")

    return vs, len(chunks)


# Example usage:
# vs, n = scrape_website(
#     ["https://example.com", "https://example.com/about"],
#     backend="chroma",                   # or "faiss"
#     persist_dir="./stores/example",
#     embedding_backend="openai",         # or "huggingface"
# )
# print(f"Indexed {n} chunks")

website_store, length = scrape_website(["https://hsbuild.com"])
website_qa = RetrievalQA.from_chain_type(llm=llm, retriever=website_store.as_retriever())

# =============== ROUTES ====================
class QueryRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(req: QueryRequest):
    query = req.query

    try:
        # 1. Try SQL Agent first
        if "artist" in query.lower() or "track" in query.lower() or "album" in query.lower():
            result = sql_agent.run(query)
            return {"source": "sql_agent", "answer": result}

        # 2. Try semantic product search
        # docs = product_store.similarity_search(query, k=2)
        # if docs:
        #     return {
        #         "source": "product_pgvector",
        #         "answer": f"I found these related products: {[d.page_content for d in docs]}"
        #     }

        # 3. Fallback: Website content
        result = website_qa.run(query)  
        return {"source": "website_docs", "answer": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

