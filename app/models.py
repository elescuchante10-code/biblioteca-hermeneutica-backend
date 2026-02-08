from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from .db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=True)
    description = Column(Text, nullable=True)

    language = Column(String, default="es", nullable=False)
    publication_year = Column(Integer, nullable=True)

    epistemological_notes = Column(Text, nullable=True)
    reading_level = Column(String, nullable=True)
    tags = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    chapters = relationship(
        "Chapter",
        back_populates="book",
        cascade="all, delete-orphan",
        order_by="Chapter.number"
    )

    reading_progress_entries = relationship(
        "ReadingProgress",
        back_populates="book",
        cascade="all, delete-orphan"
    )


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    hermeneutic_notes = Column(Text, nullable=True)

    book = relationship("Book", back_populates="chapters")

    notes = relationship(
        "Note",
        back_populates="chapter",
        cascade="all, delete-orphan"
    )


class ReadingProgress(Base):
    __tablename__ = "reading_progress"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=True)

    progress_percentage = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    book = relationship("Book", back_populates="reading_progress_entries")
    chapter = relationship("Chapter")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)

    content = Column(Text, nullable=False)
    note_type = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    chapter = relationship("Chapter", back_populates="notes")
