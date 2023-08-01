from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List


class Greats(BaseModel):
    name: str


class Book(BaseModel):
    id: UUID = uuid4()
    isbn: int
    title: List[Greats]
