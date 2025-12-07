from fastapi import FastAPI
import hashlib
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from the ITSE secure supply-chain pipeline!"}

@app.get("/hash/{text}")
def hash_text(text: str):
    """Simulate some processing to generate a hash."""
    sha = hashlib.sha256(text.encode()).hexdigest()
    return {"input": text, "sha256": sha}

@app.get("/status")
def status():
    """Simple health check endpoint."""
    return {"status": "running", "timestamp": time.time()}
