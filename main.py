from fastapi import FastAPI
from typing import List
from models import Greats, Book

app = FastAPI()

greats: List[Greats]
db: List[Book] = []


@app.get("/api/books/")
async def get_books():
    return db
