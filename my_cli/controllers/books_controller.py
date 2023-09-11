from my_cli.models.book import Book  # Import your Book model
from my_cli.utils.database import database

class BooksController:
    def add_book(self, title, author, genre, year, isbn):
        try:
            # Create a new session
            session = database.get_session()

            # Create a new book with the author's name as a string
            new_book = Book(
                title=title,
                author=author,  # Store author name as a string
                genre=genre,
                publication_year=year,
                isbn=isbn
            )
            session.add(new_book)
            session.commit()
            return new_book
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_books(self):
        try:
            # Create a new session
            session = database.get_session()

            # Query all books
            books = session.query(Book).all()
            return books
        except Exception as e:
            raise e
        finally:
            session.close()

    def update_book(self, isbn, title, author, genre, year):
        try:
            # Create a new session
            session = database.get_session()

            # Query the book by ISBN
            book = session.query(Book).filter_by(isbn=isbn).first()
            if book is None:
                return None

            # Update the book's information, including the author's name
            book.title = title
            book.author = author  # Update author name as a string
            book.genre = genre
            book.publication_year = year
            session.commit()
            return book
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_book(self, isbn):
        try:
            # Create a new session
            session = database.get_session()

            # Query the book by ISBN
            book = session.query(Book).filter_by(isbn=isbn).first()
            if book is None:
                return None

            # Delete the book
            session.delete(book)
            session.commit()
            return book
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
