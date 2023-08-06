from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from sqlalchemy.orm import declarative_base
from uuid import UUID, uuid4
from typing import List

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(ARRAY(String))
    number = Column(Integer)
    locccn = Column(Integer)
