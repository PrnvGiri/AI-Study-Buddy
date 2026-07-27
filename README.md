# 📚 AI Study Buddy (RAG Implementation)

An interactive **Retrieval-Augmented Generation (RAG)** application that converts any document (PDF or Text) into a personalized AI Study Buddy. 

Built with **LangChain**, **Chroma DB**, **Groq LLM (LLaMA 3.3)**, and a simple **Flask** Web UI.

---

## 🚀 Features
- **Document Chunking & Vector Search**: Uses `RecursiveCharacterTextSplitter` and `Chroma DB` for fast semantic retrieval.
- **Fast Inference**: Powered by Groq's high-speed LLaMA 3.3 70B model.
- **Local Embeddings**: Uses HuggingFace `all-MiniLM-L6-v2` embeddings locally.
- **Dual Interface**:
  - **CLI Script**: [`study_buddy.py`](study_buddy.py) for simple command-line querying.
  - **Web App**: [`app.py`](app.py) & [`templates/index.html`](templates/index.html) for a web-based interface.

---

## 📁 Repository Structure
```
.
├── app.py                         # Flask Web Server
├── study_buddy.py                 # Simple CLI RAG Script
├── RayOptics.pdf                  # Target Document Context
├── requirements.txt               # Dependencies for deployment
├── templates/
│   └── index.html                 # Simple HTML/CSS Frontend
├── RagImplementation31stMay2026.ipynb # Reference Notebook
├── DEPLOYMENT.md                  # Render Deployment Guide
└── README.md                      # Project Documentation
```

---

## 🛠️ Local Setup & Running

### 1. Install Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Set your Groq API Key
Copy `.env.example` to `.env` or set the environment variable:
```bash
export GROQ_API_KEY="your_groq_api_key"
```

### 3. Run the App
- **Command Line (CLI)**:
  ```bash
  python study_buddy.py
  ```
- **Web Interface**:
  ```bash
  python app.py
  ```
  Open `http://127.0.0.1:5001` in your web browser.

---

## ☁️ Deployment
For step-by-step instructions on how to deploy this application for free on Render, check out the **[DEPLOYMENT.md](DEPLOYMENT.md)** guide.
