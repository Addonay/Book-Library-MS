from sqlalchemy import Column, Integer, String, Boolean
from my_cli.utils.database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, nullable=False)  # Store author name as a string
    genre = Column(String, index=True)
    publication_year = Column(Integer)
    isbn = Column(String, unique=True, index=True)
    is_available = Column(Boolean, default=True)
