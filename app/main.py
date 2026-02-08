from fastapi import FastAPI
from .db import Base

app = FastAPI(title="Biblioteca Hermenéutica")

@app.get("/health")
def health():
    return {"status": "ok"}
