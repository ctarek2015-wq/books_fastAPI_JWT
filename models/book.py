from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import BaseModel


class BookModel(BaseModel):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    author = Column(String, unique=True)
    description = Column(String, nullable=True)

    reviews = relationship("ReviewModel", back_populates="book")
