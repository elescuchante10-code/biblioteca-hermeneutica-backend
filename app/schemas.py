from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# =========================
# BOOK SCHEMAS
# =========================

class BookBase(BaseModel):
    title: str
    author: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = "es"
    publication_year: Optional[int] = None
    epistemological_notes: Optional[str] = None
    reading_level: Optional[str] = None
    tags: Optional[list] = None


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# CHAPTER SCHEMAS
# =========================

class ChapterBase(BaseModel):
    number: int
    title: str
    content: str
    hermeneutic_notes: Optional[str] = None


class ChapterCreate(ChapterBase):
    book_id: int


class ChapterRead(ChapterBase):
    id: int
    book_id: int

    class Config:
        from_attributes = True


# =========================
# NOTE SCHEMAS
# =========================

class NoteBase(BaseModel):
    content: str
    note_type: Optional[str] = None


class NoteCreate(NoteBase):
    chapter_id: int


class NoteRead(NoteBase):
    id: int
    chapter_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# READING PROGRESS SCHEMAS
# =========================

class ReadingProgressBase(BaseModel):
    progress_percentage: int


class ReadingProgressCreate(ReadingProgressBase):
    book_id: int
    chapter_id: Optional[int] = None


class ReadingProgressRead(ReadingProgressBase):
    id: int
    book_id: int
    chapter_id: Optional[int]
    updated_at: datetime

    class Config:
        from_attributes = True


# =========================
# NESTED / DETAIL SCHEMAS
# =========================

class ChapterWithNotes(ChapterRead):
    notes: List[NoteRead] = []


class BookWithChapters(BookRead):
    chapters: List[ChapterRead] = []
