from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int

class FragmentCreate(BaseModel):
    text: str
    book_id: int

class ReadingStart(BaseModel):
    book_id: int
    start_time: str

class NoteCreate(BaseModel):
    content: str
    fragment_id: int