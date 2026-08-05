
![alt text](image.png)


# AgenticRAG 🤖📂

A simple, smart assistant that reads your personal text files and answers questions about them accurately. 


## 🗺️ How It Works (The Library Analogy)

Think of this project like a helpful assistant working in a private library:

1. **The Data Folder (`/data`):** This is your bookshelf. You drop any normal text file (`.txt`) in here, like an employee handbook or study notes.
2. **Reading & Organizing (`ingestion.py` & `indexing.py`):** The program reads your files, chops them into small paragraphs, and translates them into a "number map" that computers can read easily.
3. **Searching (`retrieval.py`):** When you ask a question (like *"What is the vacation policy?"*), the assistant instantly searches the number map to pull out the 3 best paragraphs discussing that topic.
4. **Answering (`main.py`):** The assistant hands those 3 paragraphs and your question to a smart AI model. The AI reads them and writes a clean summary on your screen.
5. **History (`logger.py`):** The assistant writes a secret note inside a file named `chat_history.log` to remember what you asked and which files were used to find the answer.

---

## 🤖 The AI Brain Used

This project connects to **OpenRouter (`openrouter/free`)** to power its answers. 

* **Why OpenRouter?** Instead of using just one AI model that might get overloaded or slow down, this settings router automatically hooks into whatever high-quality AI model is currently active, fast, and completely **FREE** to use.
* **No Lies or Hallucinations:** The AI is strictly locked down (`temperature=0.0`). We gave it strong rules: *If the answer isn't written directly inside your documents, it must say "I don't know."* It will never make up information.

---

## 🔧 How to Install and Run

### 1. What You Need
* A computer running Windows, Mac, or Linux.
* **Python 3.12 or 3.13** installed on your system.

### 2. Quick Setup Steps
Open your computer terminal or VS Code PowerShell window and run these lines one by one:

```powershell
# 1. Download this project folder
git clone https://github.com/xxxx
cd AgenticRAG

# 2. Setup a safe, isolated sandbox for Python 3.13
py -3.13 -m venv rag_env
.\rag_env\Scripts\Activate.ps1

# 3. Install the needed AI libraries
pip install openai chromadb sentence-transformers python-dotenv
```

### 3. Add Your Secret Key
Create a new file in your project folder named exactly **`.env`** and paste your OpenRouter key inside it like this:
```text
OPENROUTER_API_KEY=your-private-key-goes-here
```

---

## 🛠️ How to Use It

1. Drop your text documents inside the **`data/`** folder.
2. Start the program by running this line in your terminal:
   ```powershell
   python main.py
   ```
3. Type in any question about your files:
   ```text
   Ask a question about your documents: what is the leave policy?
   ```
4. Read your answer on screen! You can also check **`chat_history.log`** anytime to see a recording of your conversation.
