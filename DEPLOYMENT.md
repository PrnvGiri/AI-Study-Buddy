# ☁️ Deployment Guide: Render

This guide outlines step-by-step instructions for deploying the **AI Study Buddy** web application to **Render** for free.

---

## 📋 Prerequisites
1. A **GitHub account** with access to your repository: [https://github.com/PrnvGiri/AI-Study-Buddy](https://github.com/PrnvGiri/AI-Study-Buddy)
2. A free **Groq API Key** from [Groq Console](https://console.groq.com/keys)
3. A free **Render account** at [render.com](https://render.com)

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
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | `Free` |

---

### Step 4: Add Environment Variables

Scroll down to the **Environment Variables** section and click **Add Environment Variable**:

- **Key**: `GROQ_API_KEY`
- **Value**: `your_actual_groq_api_key_here`

---

### Step 5: Deploy

1. Click **Create Web Service** at the bottom.
2. Render will begin pulling your code, installing dependencies from `requirements.txt`, and launching the Gunicorn server.
3. Once the build completes, Render will provide your free HTTPS domain URL:
   `https://ai-study-buddy.onrender.com`

---

## 🎉 Verification
Visit your Render live URL, type a question about `RayOptics.pdf`, and your AI Study Buddy will respond!
