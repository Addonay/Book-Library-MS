from my_cli.models.book import Book
from my_cli.utils.database import database

class BooksController:
    def add_book(self, title, author, genre, publication_year, isbn):
        # Create a new book instance
        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            publication_year=publication_year,
            isbn=isbn
        )

        # Add the book to the database
        with database.get_session() as session:
            session.add(new_book)
            session.commit()

    def search_book(self, title):
        # Search for a book by title in the database
        with database.get_session() as session:
            book = session.query(Book).filter_by(title=title).first()
            if book:
                return book
            else:
                return None
