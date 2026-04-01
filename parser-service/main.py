from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"service": "Parser Service Running 🚀"}

# Chrome-friendly
@app.get("/parse")
def parse_get(text: str):
    words = text.split()
    return {
        "word_count": len(words),
        "keywords": words[:5]
    }

# API usage
@app.post("/parse")
def parse_post(data: InputText):
    words = data.text.split()
    return {
        "word_count": len(words),
        "keywords": words[:5]
    }
