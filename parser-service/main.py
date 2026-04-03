from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

# Custom metric
REQUEST_COUNT = Counter("parser_requests_total", "Total parser requests")

@app.get("/")
def home():
    return {"service": "Parser Running"}

@app.get("/parse")
def parse(text: str):
    REQUEST_COUNT.inc()   # increase count

    words = text.split()
    return {
        "word_count": len(words),
        "keywords": words[:5]
    }

# Metrics endpoint
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
