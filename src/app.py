from retriever import *
from fastapi import FastAPI

app = FastAPI(title="RAG API", description="Retrieve answers using OpenAI and ChromaDB", version="1.0")


@app.post("/query/")
def expose_endpont(query):
    return query_rag_system(query)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)