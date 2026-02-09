from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import Base, engine
from .routers import books, chapters, notes, reading




Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Biblioteca Hermenéutica",
    description="Backend para gestión de libros, capítulos, notas y progreso de lectura",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(chapters.router, prefix="/chapters", tags=["Chapters"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(reading.router, prefix="/reading", tags=["Reading Progress"])


@app.get("/")
def root():
    return {"status": "ok", "service": "Biblioteca Hermenéutica Backend"}
