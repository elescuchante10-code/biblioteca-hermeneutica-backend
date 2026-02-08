from fastapi import FastAPI

app = FastAPI(title="Biblioteca Hermenéutica")

@app.get("/health")
def health():
    return {"status": "ok"}
