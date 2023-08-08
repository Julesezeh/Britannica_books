from pydantic import BaseModel


class BaseBook(BaseModel):
    title: list[str] = []
    description: str | None = None
    locccn: int


class BookCreate(BaseBook):
    pass


class Book(BaseBook):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True
