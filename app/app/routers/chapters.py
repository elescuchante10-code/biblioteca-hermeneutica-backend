from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..db import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ChapterRead)
def create_chapter(
    chapter: schemas.ChapterCreate,
    db: Session = Depends(get_db)
):
    return crud.create_chapter(db, chapter)


@router.get("/book/{book_id}", response_model=List[schemas.ChapterRead])
def list_chapters_by_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_chapters_by_book(db, book_id)


@router.get("/{chapter_id}", response_model=schemas.ChapterRead)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = crud.get_chapter(db, chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter
