# retrieval.py
def retrieve_top_k(collection, question: str, top_k: int = 3) -> tuple:
    """
    Queries ChromaDB utilizing internal cosine similarity calculation 
    to retrieve the most statistically relevant information.
    """
    query_results = collection.query(
        query_texts=[question],
        n_results=top_k
    )
    
    # Extract flattened matching content
    retrieved_texts = query_results["documents"][0]
    retrieved_metadata = query_results["metadatas"][0]
    
    return retrieved_texts, retrieved_metadata
