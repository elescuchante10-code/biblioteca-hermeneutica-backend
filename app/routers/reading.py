from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from .. import crud, schemas
from ..db import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ReadingProgressRead)
def create_or_update_progress(
    progress: schemas.ReadingProgressCreate,
    db: Session = Depends(get_db)
):
    return crud.create_or_update_reading_progress(db, progress)


@router.get("/", response_model=Optional[schemas.ReadingProgressRead])
def get_progress(
    book_id: int,
    chapter_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return crud.get_reading_progress(db, book_id, chapter_id)
