class BookTemplates:
    @staticmethod
    def format_book(book):
        """Format a book as a string for display."""
        return f"Title: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPublication Year: {book.publication_year}\nISBN: {book.isbn}\nAvailability: {'Available' if book.is_available else 'Not Available'}"
