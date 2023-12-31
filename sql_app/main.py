from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .models import User
from .database import SessionLocal, engine

# First for dropping all tables, second for creating all tables
# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return {"message": "Request successful"}


@app.post("/api/v1/users/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/api/v1/users/")
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/api/v1/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/api/v1/users/{user_id}")
async def update_user(
    user_id: int, data: schemas.UserUpdate, db: Session = Depends(get_db)
):
    user = crud.update_user(user_id=user_id, data=data, db=db)
    return user


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(user_id=user_id, db=db)


@app.post("/api/v1/users/{user_id}/books/")
async def create_book_for_user(
    user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud.create_book(db=db, book=book, user_id=user_id)


@app.get("/api/v1/books/")
async def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.get("/api/v1/book/")
async def get_book_by_locccn(locccn: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_locccn(db, locccn=locccn)
    return book


@app.put("/api/v1/books/{id}/")
async def update_book(id: int, book: schemas.UpdateBook, db: Session = Depends(get_db)):
    book = crud.update_book(db, id, book)
    return book


@app.delete("/api/v1/books/{id}/")
async def delete_book(id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db=db, id=id)
    return book
