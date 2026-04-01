from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"service": "AI Service Running 🤖"}

# Chrome-friendly
@app.get("/analyze")
def analyze_get(text: str):
    score = len(text.split()) * 10
    return {
        "score": score,
        "status": "Good Resume" if score > 50 else "Needs Improvement"
    }

# API usage
@app.post("/analyze")
def analyze_post(data: InputText):
    score = len(data.text.split()) * 10
    return {
        "score": score,
        "status": "Good Resume" if score > 50 else "Needs Improvement"
    }
