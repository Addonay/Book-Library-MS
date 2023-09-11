import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_cli.utils.database import Base
from my_cli.models.book import Book

# Create an SQLite in-memory database for testing
DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database schema
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Create a new database session for each test."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_create_book(db_session):
    """Test creating a new book."""
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "genre": "Test Genre",
        "publication_year": 2022,
        "isbn": "1234567890",
        "is_available": True,
    }
    book = Book(**book_data)
    db_session.add(book)
    db_session.commit()
    
    assert book.id is not None
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.genre == "Test Genre"
    assert book.publication_year == 2022
    assert book.isbn == "1234567890"
    assert book.is_available is True

def test_update_book(db_session):
    """Test updating a book's information."""
    # Create a book
    book_data = {
        "title": "Update Test Book",
        "author": "Update Test Author",
        "genre": "Update Test Genre",
        "publication_year": 2021,
        "isbn": "9876543210",
        "is_available": True,
    }
    book = Book(**book_data)
    db_session.add(book)
    db_session.commit()

    # Update the book's information
    updated_data = {
        "title": "Updated Book Title",
        "genre": "Updated Genre",
    }
    db_session.query(Book).filter(Book.id == book.id).update(updated_data)
    db_session.commit()

    # Retrieve the updated book from the database
    updated_book = db_session.query(Book).filter(Book.id == book.id).first()

    assert updated_book.title == "Updated Book Title"
    assert updated_book.genre == "Updated Genre"

def test_delete_book(db_session):
    """Test deleting a book."""
    # Create a book
    book_data = {
        "title": "Delete Test Book",
        "author": "Delete Test Author",
        "genre": "Delete Test Genre",
        "publication_year": 2020,
        "isbn": "111122223333",
        "is_available": True,
    }
    book = Book(**book_data)
    db_session.add(book)
    db_session.commit()

    # Delete the book
    db_session.delete(book)
    db_session.commit()

    # Attempt to retrieve the deleted book
    deleted_book = db_session.query(Book).filter(Book.id == book.id).first()

    assert deleted_book is None

# You can add more test cases as needed
