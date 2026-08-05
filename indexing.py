# indexing.py
import chromadb
from config import CHROMA_COLLECTION_NAME

def initialize_vector_store(all_chunks: list):
    """
    Establishes ChromaDB collection, bundles separate metadata lists, 
    and lets Chroma automatically handle embedding conversion via miniLM.
    """
    # Create persistent or ephemeral client
    chroma_client = chromadb.Client()
    
    collection = chroma_client.create_collection(name=CHROMA_COLLECTION_NAME)
    
    # Unpack chunk dicts into unified structural arrays required by ChromaDB
    documents = [c["text"] for c in all_chunks]
    ids = [c["chunk_id"] for c in all_chunks]
    metadatas = [{"source": c["source"]} for c in all_chunks]
    
    # Internal batch injection triggers automated embedding generation
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )
    
    print(f" Successfully indexed {len(documents)} chunks to Vector DB.")
    return collection
