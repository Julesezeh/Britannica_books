from fastapi import FastAPI, HTTPException
from typing import List
from models import Book, UpdateBook
from uuid import UUID, uuid4

app = FastAPI()

db: List[Book] = [
    Book(locccn=1313, number=13, title=["Plato", "Bih"]),
    Book(locccn=1213, number=14, title=["Aristotle", "Bih"]),
]


@app.get("/api/books/")
async def get_books():
    return db


@app.post("/api/books/")
async def add_book(book: Book):
    for greats in db:
        if greats.title == book.title:
            return HTTPException(
                status_code=400, detail=f"Book title {book.title} already exists"
            )
        if greats.locccn == book.locccn:
            return HTTPException(
                status_code=400,
                detail=f"Book with library of congress catalog card number {book.locccn} already exists",
            )

    db.append(book)
    return db


@app.delete("/api/books/{id}")
async def delete_book(id: UUID):
    for book in db:
        if book.id == id:
            db.remove(book)
            return book
    return HTTPException(
        status_code=400, detail=f"Book with id {id} could not be found"
    )


@app.put("/api/books/{id}")
async def update_book(id: UUID, book_update: UpdateBook):
    for book in db:
        if book.id == book_update.id:
            if book_update.title:
                book.title = book_update.title
            if book_update.number:
                book.number = book_update.number
            if book_update.locccn:
                book.locccn = book_update.locccn
            return 200
    return HTTPException(status_code=400, detail=f"Book with id {id} does not exist")
