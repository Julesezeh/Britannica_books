from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user


def update_user(db: Session, user_id: int, data: schemas.UserUpdate):
    user = db.query(models.User).get(user_id)
    if user:
        print(user)
        if data.email:
            user.email = data.email
        if data.is_active:
            user.is_active = data.is_active

        db.add(user)
        db.commit()
        db.refresh(user)

        return user, 200
    else:
        raise HTTPException(detail=f"User with id {user_id} not found", status_code=404)


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter_by(id=user_id)
    if user:
        db.delete(user)
        db.commit()
        return None, 204
    else:
        raise HTTPException(f"User with id {id} not found")


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_item = models.Book(**book.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item


def get_book_by_locccn(db: Session, locccn: int):
    book = db.query(models.Book).filter_by(locccn=locccn)[:]
    if book:
        return book
    else:
        raise HTTPException(
            status_code=404, detail=f"Book with locccn {locccn} not found"
        )


def update_book(db: Session, id: int, book: schemas.UpdateBook):
    existing_book = db.query(models.Book).filter_by(id=id)[0]
    if existing_book:
        if book.title:
            existing_book.title = book.title
        if book.locccn:
            existing_book.locccn = book.locccn
        print(existing_book)
        db.add(existing_book)
        db.commit()
        db.refresh(existing_book)
        db.close()
        return existing_book
    raise HTTPException(status_code=404, detail="File not found")


def delete_book(db: Session, id: int):
    db_book = db.query(models.Book).filter_by(id=id)[0]
    if db_book:
        db.delete(db_book)
        db.commit()
        return None, 204
    else:
        raise HTTPException("Book with id {id} not found")
