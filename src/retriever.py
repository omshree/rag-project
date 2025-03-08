from openai import OpenAI
import openai
from parsing_chunking import *


collection_name = 'ubuntu-doc-v03'

doc_index = get_index_from_collection(collection_name)



client = OpenAI(
    api_key=openai.api_key
)

def query_rag_system(query):
    # doc_index = get_index_from_collection(collection_name)
    retriever = doc_index.as_retriever(similarity_top_k=10)
    retrieved_nodes = retriever.retrieve(query)
    
    # Extract top 10 relevant chunks
    context = "\n\n".join([node.text for node in retrieved_nodes])
    system_prompt = {"role": "system", "content": "You are a helpful assistant. Answer based on the provided context. you will also be provided with the privious"}
    # Step 5: Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            system_prompt,
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ],
        temperature=0.7,
    )

    return {"role": "assistant", "content": response.choices[0].message.content}


