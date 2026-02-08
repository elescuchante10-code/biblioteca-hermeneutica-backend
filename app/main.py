from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .db import Base, engine, SessionLocal
from .models import Book

app = FastAPI(title="Biblioteca Hermenéutica")


# --- creación explícita de tablas ---
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# --- dependencia de base de datos ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- esquema de entrada ---
class BookCreate(BaseModel):
    title: str
    author: str | None = None
    description: str | None = None


# --- endpoint de salud ---
@app.get("/health")
def health():
    return {"status": "ok"}


# --- acto de inscripción del libro ---
@app.post("/books")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        author=book.author,
        description=book.description
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {
        "message": "Libro inscrito en la biblioteca",
        "book_id": new_book.id
    }
