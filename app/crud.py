from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas


# =========================
# BOOK CRUD
# =========================

def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session) -> List[models.Book]:
    return db.query(models.Book).all()


def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    return db.query(models.Book).filter(models.Book.id == book_id).first()


# =========================
# CHAPTER CRUD
# =========================

def create_chapter(db: Session, chapter: schemas.ChapterCreate) -> models.Chapter:
    db_chapter = models.Chapter(**chapter.model_dump())
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


def get_chapters_by_book(db: Session, book_id: int) -> List[models.Chapter]:
    return (
        db.query(models.Chapter)
        .filter(models.Chapter.book_id == book_id)
        .order_by(models.Chapter.number)
        .all()
    )


def get_chapter(db: Session, chapter_id: int) -> Optional[models.Chapter]:
    return db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()


# =========================
# NOTE CRUD
# =========================

def create_note(db: Session, note: schemas.NoteCreate) -> models.Note:
    db_note = models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_notes_by_chapter(db: Session, chapter_id: int) -> List[models.Note]:
    return (
        db.query(models.Note)
        .filter(models.Note.chapter_id == chapter_id)
        .order_by(models.Note.created_at)
        .all()
    )


# =========================
# READING PROGRESS CRUD
# =========================

def create_or_update_reading_progress(
    db: Session,
    progress: schemas.ReadingProgressCreate
) -> models.ReadingProgress:

    existing = (
        db.query(models.ReadingProgress)
        .filter(
            models.ReadingProgress.book_id == progress.book_id,
            models.ReadingProgress.chapter_id == progress.chapter_id
        )
        .first()
    )

    if existing:
        existing.progress_percentage = progress.progress_percentage
        db.commit()
        db.refresh(existing)
        return existing

    db_progress = models.ReadingProgress(**progress.model_dump())
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress


def get_reading_progress(
    db: Session,
    book_id: int,
    chapter_id: Optional[int] = None
) -> Optional[models.ReadingProgress]:

    query = db.query(models.ReadingProgress).filter(
        models.ReadingProgress.book_id == book_id
    )

    if chapter_id is not None:
        query = query.filter(models.ReadingProgress.chapter_id == chapter_id)

    return query.first()
