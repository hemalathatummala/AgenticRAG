# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter Credentials
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
SITE_URL = os.getenv("SITE_URL", "https://localhost:3000")
APP_NAME = os.getenv("APP_NAME", "LocalRAG")

# Swap out the OpenAI model name for a high-quality, completely FREE OpenRouter model identifier
# Popular free options: "meta-llama/llama-3-8b-instruct:free" or "google/gemma-2-9b-it:free"
LLM_MODEL = "openrouter/free"

# Vector Database Settings (Remains exactly the same)
CHROMA_COLLECTION_NAME = "company_docs"
