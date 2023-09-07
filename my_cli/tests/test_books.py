import unittest
from my_cli.controllers.books_controller import BooksController
from my_cli.models.book import Book
from my_cli.utils.database import database

class TestBooksController(unittest.TestCase):
    def setUp(self):
        # Initialize the database and controller
        database.create_tables()
        self.books_controller = BooksController()

    def tearDown(self):
        # Clear the database after each test
        with database.get_session() as session:
            session.query(Book).delete()

    def test_add_book(self):
        # Test adding a book
        self.books_controller.add_book(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            publication_year=2023,
            isbn="1234567890"
        )

        # Verify that the book is added to the database
        with database.get_session() as session:
            book = session.query(Book).filter_by(title="Test Book").first()
            self.assertIsNotNone(book)
            self.assertEqual(book.title, "Test Book")
            self.assertEqual(book.author, "Test Author")
            self.assertEqual(book.genre, "Test Genre")
            self.assertEqual(book.publication_year, 2023)
            self.assertEqual(book.isbn, "1234567890")

    def test_search_book(self):
        # Add a test book to the database
        with database.get_session() as session:
            test_book = Book(
                title="Test Book",
                author="Test Author",
                genre="Test Genre",
                publication_year=2023,
                isbn="1234567890"
            )
            session.add(test_book)

        # Test searching for the added book
        found_book = self.books_controller.search_book("Test Book")
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.title, "Test Book")

if __name__ == '__main__':
    unittest.main()
