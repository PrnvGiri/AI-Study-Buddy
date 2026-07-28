# ☁️ Deployment Guide: Hugging Face Spaces (Gradio)

This guide outlines step-by-step instructions for deploying the **AI Study Buddy** Gradio web application for free.

---

## 🛠️ Option 1: Hugging Face Spaces (Recommended for Gradio)

### Step 1: Create a Space
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and log in.
2. Click **Create new Space**.
3. Configure settings:
   - **Space Name**: `ai-study-buddy`
   - **SDK**: Select **Gradio**
   - **Hardware**: **CPU Basic (Free)**

### Step 2: Add Files & Secret Key
1. Upload/Sync your repository files: `app.py`, `RayOptics.pdf`, `requirements.txt`.
2. Go to **Settings -> Secrets**:
   - Add Secret Name: `GROQ_API_KEY`
   - Add Secret Value: `your_actual_groq_api_key_here`

Your app will automatically build and launch at `https://huggingface.co/spaces/your-username/ai-study-buddy`.
