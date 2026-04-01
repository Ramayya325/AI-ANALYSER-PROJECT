from fastapi import FastAPI
import requests

app = FastAPI()

PARSER_URL = "http://parser-service:8001"
AI_URL = "http://ai-service:8000"

@app.get("/")
def home():
    return {"service": "API Gateway Running 🌐"}

# Chrome-friendly full flow
@app.get("/analyze")
def full_analysis(text: str):
    parser_res = requests.get(f"{PARSER_URL}/parse", params={"text": text}).json()
    ai_res = requests.get(f"{AI_URL}/analyze", params={"text": text}).json()

    return {
        "parser_output": parser_res,
        "ai_output": ai_res
    }
