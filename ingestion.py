# ingestion.py
import os

def chunk_text(text: str, source_name: str) -> list:
    """
    Divides raw text strings into chunk dictionaries.
    """
    paragraphs = text.strip().split("\n\n")
    chunks = []
    
    for i, para in enumerate(paragraphs):
        clean_para = para.strip()
        
        # Skip small artifact lines or divider headers
        if len(clean_para) < 50 or clean_para.startswith("="):
            continue
            
        chunks.append({
            "text": clean_para,
            "source": source_name,
            "chunk_id": f"{source_name}_chunk_{i}"
        })
        
    return chunks


def load_documents_from_folder(folder_path: str = "data") -> list:
    """
    Loops through the data/ folder, reads all .txt documents, 
    and returns a combined list of all processed text chunks.
    """
    all_chunks = []
    
    # Check if the folder exists to prevent crashes
    if not os.path.exists(folder_path):
        print(f"⚠️ Error: The folder '{folder_path}' does not exist yet. Please create it.")
        return all_chunks

    # Read each file inside the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            print(f"📖 Reading document: {filename}")
            with open(file_path, "r", encoding="utf-8") as file:
                raw_text = file.read()
                
            # Chunk the file's text and add it to our master list
            file_chunks = chunk_text(raw_text, source_name=filename)
            all_chunks.extend(file_chunks)
            
    return all_chunks
