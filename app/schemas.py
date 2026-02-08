from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    published_date: str


class FragmentCreate(BaseModel):
    book_id: int
    text: str
    page_number: int


class ReadingStart(BaseModel):
    user_id: int
    book_id: int
    start_time: str


class NoteCreate(BaseModel):
    fragment_id: int
    user_id: int
    content: str
    created_at: str