# 📚 AI Study Buddy (RAG Implementation)

An interactive **Retrieval-Augmented Generation (RAG)** application that converts any document (PDF or Text) into a personalized AI Study Buddy. 

Built with **LangChain**, **Chroma DB**, **Groq LLM (LLaMA 3.3)**, and **Gradio**.

---

## 🚀 Features
- **Document Chunking & Vector Search**: Uses `RecursiveCharacterTextSplitter` and `Chroma DB` for fast semantic retrieval.
- **Fast Inference**: Powered by Groq's high-speed LLaMA 3.3 70B model.
- **Local Embeddings**: Uses HuggingFace `all-MiniLM-L6-v2` embeddings locally.
- **Dual Interface**:
  - **Gradio Web App**: [`app.py`](app.py) for interactive web interface (`demo.launch(share=True)`).
  - **CLI Script**: [`study_buddy.py`](study_buddy.py) for simple command-line querying.

---

## 📁 Repository Structure
```
.
├── app.py                         # Gradio Web Application
├── study_buddy.py                 # Simple CLI RAG Script
├── RayOptics.pdf                  # Target Document Context
├── requirements.txt               # Dependencies list
├── .env.example                   # Environment variable template
├── RagImplementation31stMay2026.ipynb # Reference Notebook
├── DEPLOYMENT.md                  # Deployment Guide
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
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Add your key inside `.env`:
```env
GROQ_API_KEY="your_groq_api_key"
```

### 3. Run the App
- **Gradio Web Interface**:
  ```bash
  python app.py
  ```
  Generates both local URL (`http://127.0.0.1:7860`) and a free public share URL (`https://xxxx.gradio.live`).

- **Command Line (CLI)**:
  ```bash
  python study_buddy.py
  ```

---

## ☁️ Deployment
For instructions on deploying this application for free on Hugging Face Spaces or Render, check out the **[DEPLOYMENT.md](DEPLOYMENT.md)** guide.
