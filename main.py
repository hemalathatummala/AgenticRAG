# main.py
from openai import OpenAI
import config
from ingestion import load_documents_from_folder
from indexing import initialize_vector_store
from retrieval import retrieve_top_k
from logger import log_interaction 


# main.py
def assemble_and_run_rag(question: str, collection, openai_client):
    # Fetch supporting documents
    context_chunks, metadata = retrieve_top_k(collection, question, top_k=3)
    combined_context = "\n".join(context_chunks)
    
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that answers questions based ONLY on the provided context. "
                "If the context does not contain enough information to answer, strictly reply with: "
                "'I don't have enough context or information to answer this question.' "
                "Do not make up information or assume anything."
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{combined_context}\n\nQuestion: {question}"
        }
    ]
    
    try:
        response = openai_client.chat.completions.create(
            model=config.LLM_MODEL,
            messages=messages,
            temperature=0.0
        )
        
        # -----------------------------------------------------------------
        #  FIX: Dynamically parse either list items or object models safely
        # -----------------------------------------------------------------
        if not response or not hasattr(response, 'choices') or len(response.choices) == 0:
            ai_answer = "❌ Error: Received an empty payload response from the server."
        else:
            first_choice = response.choices[0]
            
            # Check if OpenRouter packaged the choice as a standard Python dictionary
            if isinstance(first_choice, dict):
                ai_answer = first_choice.get("message", {}).get("content", "❌ Empty dictionary message string context.")
            # Check if it's a standard dictionary that needs index lookup values
            elif hasattr(first_choice, 'get'):
                ai_answer = first_choice.get("message", {}).get("content", "❌ Dictionary model lookup failed.")
            # Fallback scenario: Standard typed class object format
            else:
                ai_answer = first_choice.message.content

        # Pass the extracted text down into your logger module smoothly
        log_interaction(question, context_chunks, metadata, ai_answer)
        return ai_answer

    except Exception as e:
        error_msg = f"❌ OpenRouter Connection Error: {str(e)}"
        log_interaction(question, [], [], error_msg)
        return error_msg


if __name__ == "__main__":
    print("Initializing OpenRouter Client...")
    
    # Correct Base URI structure for OpenRouter integrations
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=config.OPENROUTER_API_KEY,
        default_headers={
            "HTTP-Referer": config.SITE_URL,
            "X-Title": config.APP_NAME,
        }
    )
    
    print("\nStep 1: Reading data from the 'data/' folder...")
    all_document_chunks = load_documents_from_folder("data")
    
    if not all_document_chunks:
        print("❌ Stop: No chunks were loaded. Check if your data/ folder has .txt files.")
        exit()
        
    print(f"Step 2: Hydrating Vector Store with {len(all_document_chunks)} chunks...")
    v_db_collection = initialize_vector_store(all_document_chunks)
    
    print("\n--- Pipeline Ready ---")
    while True:
        user_query = input("\nAsk a question about your documents (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
            
        answer = assemble_and_run_rag(user_query, v_db_collection, client)
        print(f"\nAnswer:\n{answer}")
