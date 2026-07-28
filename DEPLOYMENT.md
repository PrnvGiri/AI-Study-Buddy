# ☁️ Deployment Guide: Streamlit

This guide outlines step-by-step instructions for deploying your **AI Study Buddy** Streamlit web application.

---

## 🌟 Method 1: Streamlit Community Cloud (Recommended - 100% Free ⭐)

Streamlit offers official **100% free hosting** for Streamlit apps directly from GitHub.

### Step-by-Step Instructions:
1. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with your **GitHub account**.
2. Click **New app**.
3. Select your repository: `PrnvGiri/AI-Study-Buddy`, Branch: `main`, Main file path: `app.py`.
4. Click **Advanced settings** -> **Secrets** and add:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
5. Click **Deploy!** Your app will be live at a free URL: `https://ai-study-buddy.streamlit.app`.

---

## ⚡ Method 2: Render Deployment

If deploying to **Render**:

| Setting | Value |
| :--- | :--- |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

### Environment Variable:
- **Key**: `GROQ_API_KEY`
- **Value**: `your_actual_groq_api_key_here`
