
![alt text](image.png)

🤖 I just built and open-sourced a custom Retrieval-Augmented Generation (RAG) pipeline! 📂
To understand the core architecture behind grounding Large Language Models on private data, I built AgenticRAG—a modular system designed to completely eliminate AI hallucinations.
Here is the exact technical workflow under the hood:
***1️⃣ Ingestion: Text documents are parsed and broken down into small, optimized chunks.
***2️⃣ Embedding & Vector Storage: These chunks are processed by Chroma DB, which automatically generates vector embeddings underneath to index the data.
***3️⃣ Semantic Retrieval: When a query is submitted, the pipeline retrieves the top 3 most relevant chunks based on vector cosine similarity.
***4️⃣ Grounded Generation: These 3 chunks are injected directly into the LLM context window as a strict reference frame.
By pairing this context with a zero-temperature setting (temperature=0.0) and strict system prompt guidelines, the LLM is forced to respond using only the provided text, effectively preventing hallucinations
