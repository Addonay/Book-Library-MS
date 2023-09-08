from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from my_cli.utils.database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    genre = Column(String, index=True)
    publication_year = Column(Integer)
    isbn = Column(String, unique=True, index=True)
    is_available = Column(Boolean, default=True)

    # Define the relationship with the Author model
    author = relationship("Author", back_populates="books")
