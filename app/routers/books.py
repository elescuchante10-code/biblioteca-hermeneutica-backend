from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..db import SessionLocal

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.BookRead)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
):
    return crud.create_book(db, book)


@router.get("/", response_model=List[schemas.BookRead])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
