# ☁️ Deployment Guide: Render

This guide outlines step-by-step instructions for deploying the **AI Study Buddy** Flask web application to **Render** for free.

---

## 📋 Prerequisites
1. A **GitHub account** with access to your repository: [https://github.com/PrnvGiri/AI-Study-Buddy](https://github.com/PrnvGiri/AI-Study-Buddy)
2. A free **Groq API Key** from [Groq Console](https://console.groq.com/keys)
3. A free **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey)
4. A free **Render account** at [render.com](https://render.com)

---

## 🛠️ Step-by-Step Instructions

### Step 1: Log in to Render
1. Go to [https://render.com](https://render.com) and log in using your **GitHub account**.

---

### Step 2: Create a New Web Service
1. Click the **New +** button at the top right of the Render Dashboard.
2. Select **Web Service**.
3. Choose **Build and deploy from a Git repository**.
4. Click **Connect** next to your repository: `PrnvGiri/AI-Study-Buddy`.

---

### Step 3: Configure Service Settings

Fill in the deployment settings as follows:

| Setting | Value |
| :--- | :--- |
| **Name** | `ai-study-buddy` (or any custom name) |
| **Region** | Choose nearest (e.g. Oregon, Frankfurt, Singapore) |
| **Branch** | `main` |
| **Root Directory** | *(leave blank)* |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn --bind 0.0.0.0:$PORT app:app` |
| **Instance Type** | `Free` |

> 💡 **Important**: Make sure the **Start Command** is set to `gunicorn --bind 0.0.0.0:$PORT app:app`.

---

### Step 4: Add Environment Variables

Scroll down to the **Environment Variables** section and click **Add Environment Variable** for both keys:

1. **Groq Key**:
   - **Key**: `GROQ_API_KEY`
   - **Value**: `your_actual_groq_api_key_here`

2. **Google Key**:
   - **Key**: `GOOGLE_API_KEY`
   - **Value**: `your_actual_google_api_key_here`

---

### Step 5: Deploy

1. Click **Create Web Service** at the bottom.
2. Render will pull your repository, install the lightweight dependencies from `requirements.txt`, and launch Gunicorn.
3. Because we use Google API Embeddings instead of heavy PyTorch weights, your app will use **< 50MB of RAM** and run smoothly without memory errors!
4. Render will provide your free HTTPS domain URL:
   `https://ai-study-buddy.onrender.com`
