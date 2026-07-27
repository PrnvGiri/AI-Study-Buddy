# 🎓 AI Study Buddy (Basic RAG Implementation)

A simple, easy-to-understand Retrieval-Augmented Generation (RAG) program built with **LangChain**, **Chroma DB**, and **Groq LLM**.

Simply put any document (`.txt`, `.pdf`, `.md`) into the program, and it immediately becomes an interactive AI Study Buddy ready to answer your questions, explain concepts, and quiz you on the study material!

---

## 🛠️ Stack & Architecture
- **LLM**: Groq API (`llama-3.3-70b-versatile`) via `langchain-groq`
- **Vector Database**: Chroma DB (`langchain-chroma`)
- **Embeddings**: `all-MiniLM-L6-v2` via `langchain-huggingface` (Runs 100% locally, no extra embedding key required)
- **Document Chunking**: `RecursiveCharacterTextSplitter` (1000 char chunks, 200 char overlap)

---

## 🚀 Getting Started

### 1. Get a Free Groq API Key
1. Go to [Groq Console](https://console.groq.com/keys) and sign up for a free account.
2. Create an API Key.
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Add your API Key into `.env`:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

### 2. Run the Study Buddy
Run the script with the default sample notes (`sample_notes.txt`):
```bash
.venv/bin/python study_buddy.py
```

Or pass your own document (PDF or Text):
```bash
.venv/bin/python study_buddy.py /path/to/your_chapter.pdf
```

---

## 💻 How It Works (4 Basic Steps)

1. **Document Loading**: Reads text or PDF file using LangChain's loaders (`TextLoader` / `PyPDFLoader`).
2. **Text Chunking**: Breaks large documents into small bite-sized chunks so the LLM can search effectively.
3. **Vector Store (Chroma DB)**: Converts chunks into numerical vector embeddings and saves them locally in `./chroma_db`.
4. **RAG Retrieval & Response**: When you ask a question, Chroma DB retrieves the top 3 relevant context chunks, and passes them to **Groq LLM (LLaMA 3.3)** to produce an accurate answer based on your notes.
