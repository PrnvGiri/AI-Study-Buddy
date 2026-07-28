# 📚 AI Study Buddy (RAG Implementation)

An interactive **Retrieval-Augmented Generation (RAG)** application that converts any document (PDF or Text) into a personalized AI Study Buddy. 

Built with **LangChain**, **Chroma DB**, **Groq LLM (LLaMA 3.3)**, and **Streamlit**.

---

## 🚀 Features
- **Document Chunking & Vector Search**: Uses `RecursiveCharacterTextSplitter` and `Chroma DB` for fast semantic retrieval.
- **Fast Inference**: Powered by Groq's high-speed LLaMA 3.3 70B model.
- **Local Embeddings**: Uses HuggingFace `all-MiniLM-L6-v2` embeddings locally.
- **Streamlit Web UI**: Interactive chat interface with session history and resource caching.

---

## 📁 Repository Structure
```
.
├── app.py                         # Streamlit Web Application
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
Copy `.env.example` to `.env` and add your key:
```bash
cp .env.example .env
```
Inside `.env`:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Streamlit App
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your web browser.

---

## ☁️ Free Deployment
For step-by-step instructions on how to deploy this application for free, check out the **[DEPLOYMENT.md](DEPLOYMENT.md)** guide.
