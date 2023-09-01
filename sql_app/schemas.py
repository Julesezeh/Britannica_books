from pydantic import BaseModel
from typing import List


class BaseBook(BaseModel):
    title: str
    locccn: int


class BookCreate(BaseBook):
    pass


class UpdateBook(BaseBook):
    title: str = None
    locccn: int = None


class Book(BaseBook):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    is_active: bool


class User(UserBase):
    id: int
    is_active: bool
    books: List[Book] = []

    class Config:
        from_attributes = True
