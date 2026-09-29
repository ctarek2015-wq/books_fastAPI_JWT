from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel
from .book import BookModel


class ReviewModel(BaseModel):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    content = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    user = relationship("UserModel", back_populates="reviews")
    book = relationship("BookModel", back_populates="reviews")
