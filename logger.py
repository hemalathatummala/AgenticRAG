# logger.py
from datetime import datetime
import os

LOG_FILE = "chat_history.log"

def log_interaction(question: str, context_chunks: list, metadata_list: list, answer: str):
    """
    Appends a detailed conversation timestamp report safely into a local log file.
    Guaranteed not to throw AttributeErrors or KeyErrors.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 🕵️ Safe, crash-proof extraction of source names
    sources = set()
    if metadata_list:
        for meta in metadata_list:
            if isinstance(meta, dict):
                # Try common metadata naming variations
                source_val = meta.get("source") or meta.get("filename") or meta.get("file")
                if source_val:
                    sources.add(str(source_val))
            elif isinstance(meta, (list, tuple)) and len(meta) > 0:
                # If metadata is a nested list/tuple, grab the first element
                sources.add(str(meta[0]))
            elif meta:
                # Fallback string representation
                sources.add(str(meta))
                
    sources_str = ", ".join(sources) if sources else "Unknown / None"

    # Build a clean text log block
    log_entry = (
        f"==================================================\n"
        f"📅 TIMESTAMP: {timestamp}\n"
        f"❓ QUESTION:  {question}\n"
        f"📖 SOURCES:   {sources_str}\n"
        f"--------------------------------------------------\n"
        f"🤖 ANSWER:\n{str(answer).strip()}\n"
        f"==================================================\n\n"
    )

    # Append the entry smoothly to the file
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_entry)
    except Exception as e:
        print(f"⚠️ Warning: Could not write to log file: {e}")

