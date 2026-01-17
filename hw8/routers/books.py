from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from schemas.books import Book, BookCreate, BookUpdate

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

books_db: List[Book] = []
current_id = 1

@router.post("/", response_model=Book)
def create_book(book: BookCreate):
    global current_id

    new_book = Book(id=current_id, **book.model_dump())
    books_db.append(new_book)
    current_id += 1
    return new_book

@router.get("/", response_model=List[Book])
def read_all_books(
    author: Optional[str] = Query(default=None),
    year: Optional[int] = Query(default=None)
):
    books = books_db

    if author:
        books = [b for b in books if b.author == author]
    if year:
        books = [b for b in books if b.year == year]

    return books

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@router.get("/by-tag/{tag}", response_model=List[Book])
def read_by_tag(tag: str):
    books = [b for b in books_db if b.tags and tag in b.tags]

    if not books:
        raise HTTPException(status_code=404, detail="Books with this tag not found")

    return books

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            update_book = book.model_copy(update=book_update.model_dump(exclude_unset=True))
            books_db[index] = update_book
            return update_book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}", response_model=Book)
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            return books_db.pop(index)

    raise HTTPException(status_code=404, detail="Book not found")
