from fastapi import APIRouter, Depends
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


@router.post("/", response_model=schemas.NoteRead)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db)
):
    return crud.create_note(db, note)


@router.get("/chapter/{chapter_id}", response_model=List[schemas.NoteRead])
def list_notes_by_chapter(
    chapter_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_notes_by_chapter(db, chapter_id)
