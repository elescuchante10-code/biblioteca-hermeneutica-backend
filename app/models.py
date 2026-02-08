from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=True)
    description = Column(Text, nullable=True)

    fragments = relationship("Fragment", back_populates="book")
    reading_states = relationship("ReadingState", back_populates="book")


class Fragment(Base):
    __tablename__ = "fragments"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    order = Column(Integer, nullable=False)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=True)

    book = relationship("Book", back_populates="fragments")
    notes = relationship("Note", back_populates="fragment")


class ReadingState(Base):
    __tablename__ = "reading_states"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    fragment_id = Column(Integer, ForeignKey("fragments.id"), nullable=True)

    progress = Column(Integer, nullable=True)
    active = Column(Boolean, default=True)
    last_read_at = Column(DateTime, default=datetime.utcnow)

    book = relationship("Book", back_populates="reading_states")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    fragment_id = Column(Integer, ForeignKey("fragments.id"), nullable=False)

    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    fragment = relationship("Fragment", back_populates="notes")