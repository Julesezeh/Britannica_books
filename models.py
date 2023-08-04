from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List


# locccn-->library of congress catalog card number
class Book(BaseModel):
    id: UUID = uuid4()
    number: int
    locccn: int
    title: List[str]


class UpdateBook(BaseModel):
    id: UUID = None
    number: int = None
    locccn: int = None
    title: List[str] = None
