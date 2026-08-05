import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the single .env file
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

print("--- DIAGNOSTIC CHECK ---")
print(f"API Key found in .env: {api_key is not None}")
if api_key:
    print(f"Key starts with: {api_key[:12]}...")

print("\nConnecting to OpenRouter server...")

# 2. Build the exact same client setup
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "DiagnosticCheck",
    }
)

# 3. Request a minimal string response using a free model
try:
    response = client.chat.completions.create(
        model="google/gemma-2-9b-it:free",
        messages=[{"role": "user", "content": "Say the word 'Working'"}],
        temperature=0.0
    )
    
    # Check if the server returned an error string instead of an object
    if isinstance(response, str):
        print("\n❌ Connected to server, but OpenRouter returned a raw text error:")
        print(f"👉 Error message: {response}")
    else:
        print("\n✅ API IS WORKING PERFECTLY!")
        print(f"Response from AI: {response.choices[0].message.content}")

except Exception as e:
    print(f"\n❌ Python SDK Connection crashed with exception:")
    print(e)
