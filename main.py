import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

# 1. PUT YOUR API KEY HERE (Keep the quotation marks!)
os.environ["GROQ_API_KEY"] = "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"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. We tell the AI exactly what fields to hunt for in your sentence
class ExtractedInfo(BaseModel):
    hcpName: str = Field(description="The name of the doctor or healthcare professional")
    topicsDiscussed: str = Field(description="A brief summary of what was discussed")
    sentiment: str = Field(description="Must be exactly one of these words: Positive, Neutral, or Negative")

# 3. We load the Gemma 2 model
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
# This forces the AI to reply in our exact React format, not a normal paragraph!
structured_llm = llm.with_structured_output(ExtractedInfo)

class ChatRequest(BaseModel):
    user_input: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # The AI reads your chat and extracts the variables
        ai_extracted_data = structured_llm.invoke(request.user_input)
        
        return {
            "reply": f"Got it! I've updated the form with the details for {ai_extracted_data.hcpName}.",
            "extracted_data": ai_extracted_data.dict() # Sends the data straight to Redux!
        }
    except Exception as e:
        # If the AI gets confused by the sentence, it won't crash the app
        print(f"AI Error: {e}")
        return {
            "reply": "I couldn't quite catch all the details from that. Could you rephrase it?",
            "extracted_data": None
        }