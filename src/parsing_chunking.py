import os
import chromadb
from llama_index.readers.file import MarkdownReader

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext, Document
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter, HierarchicalNodeParser
from llama_index.core.ingestion import IngestionPipeline

import chromadb
import nest_asyncio
nest_asyncio.apply()

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en")

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=1024, chunk_overlap=100),
    ]
)

# Function to Recursively Find `.md` Files
def find_md_files(root_folder):
    md_files = []
    for folder_path, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".md"):
                full_path = os.path.join(folder_path, filename)
                relative_path = os.path.relpath(full_path, root_folder)
                md_files.append((full_path, relative_path))
    return md_files

# Load and Chunk Markdown Files
def process_md_files(md_files):
    nodes = []

    for file_path, relative_path in md_files:
        documents = MarkdownReader().load_data(file_path)
        file_nodes = pipeline.run(documents=documents)
    

        # Add metadata (folder structure)
        for node in file_nodes:
            node.metadata = {"folder_path": relative_path}
            nodes.append(node)

    return nodes



# Connect to ChromaDB
def get_index_from_collection(collection_name):
    chroma_client = chromadb.PersistentClient(path="../chroma_db")
    try:
        collection = chroma_client.get_collection(name=collection_name)
        print('using existing collection ')
        nodes = collection.get()
        documents = [Document(text=text, metadata=metadata) for text, metadata in zip(nodes['documents'], nodes['metadatas'])]
        vector_store = ChromaVectorStore(chroma_collection=collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        doc_index = VectorStoreIndex.from_documents(
            documents, embed_model=embed_model, show_progress=True
        )
        
    except:
        print('collection is not found.. creating new')
        collection = chroma_client.get_or_create_collection(name=collection_name)

        # Read and Store Markdown Files
        root_folder = "../data/demo_bot_data/ubuntu-docs"  
        md_files = find_md_files(root_folder)  
        nodes = process_md_files(md_files)  
        vector_store = ChromaVectorStore(chroma_collection=collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        doc_index = VectorStoreIndex(
            nodes, storage_context=storage_context, embed_model=embed_model, show_progress=True
        )

    return doc_index