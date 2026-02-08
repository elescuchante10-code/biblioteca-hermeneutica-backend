from fastapi import FastAPI

from .db import Base, engine
from . import models  # necesario para que Base registre las tablas

app = FastAPI(title="Biblioteca Hermenéutica")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}
