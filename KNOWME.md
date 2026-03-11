# 🩺 AI-First CRM: HCP Interaction Module

An intelligent, full-stack CRM module designed for the Life Sciences and Healthcare domain. This application eliminates manual data entry for pharmaceutical sales representatives by using a Large Language Model (LLM) to automatically parse natural conversation and extract structured data (HCP Name, Topics Discussed, Sentiment).



## ✨ Key Features
* **Natural Language Processing:** Type conversational summaries, and the AI will extract the necessary variables.
* **Structured AI Output:** Uses LangChain and Pydantic schemas to force the LLM to return strict, predictable JSON data instead of conversational text.
* **Real-Time UI Updates:** Integrated with Redux Toolkit to instantly update the React frontend the moment the AI finishes processing.
* **Bulletproof CORS:** Configured FastAPI middleware for secure cross-origin communication between the frontend and backend.

## 🛠️ Tech Stack
**Frontend:**
* React (UI Components)
* Redux Toolkit (State Management)
* Axios (API Communication)
* CSS (Styling)

**Backend:**
* Python
* FastAPI (API Server)
* Uvicorn (ASGI Web Server)

**AI & Machine Learning:**
* LangChain Core (Orchestration)
* Groq Cloud API (Lightning-fast inference)
* Llama 3.1 8B (LLM)

---

## 🚀 How to Run the Project Locally

To run this full-stack application, you will need to open **two separate terminal windows**—one for the Python backend and one for the React frontend.

### 1. Backend Setup (FastAPI + AI)
First, you need a free API key from [Groq Cloud](https://console.groq.com/keys). Once you have it, open `main.py` and replace `"YOUR_API_KEY_HERE"` with your actual key.

Open a terminal in the root directory and run:
```bash
# Install required Python dependencies
pip install fastapi uvicorn pydantic langchain-groq langchain-core

# Start the FastAPI server
python -m uvicorn main:app --reload

The backend will be running at http://127.0.0.1:8000




2. Frontend Setup (React)
Open a second terminal, navigate to the React src directory, and run:

# Install required Node dependencies
npm install @reduxjs/toolkit react-redux axios

# Start the development server
npm start

The React app will automatically open in your browser at http://localhost:3000







🧪 Testing the AI
Once both servers are running, type the following into the AI Assistant chat box and click Log:

"I just had a great meeting with Dr. Sarah Jenkins. We talked about the new clinical trials for the heart medication, and she seemed very enthusiastic about it."

Watch the form instantly auto-fill with the extracted entities!
