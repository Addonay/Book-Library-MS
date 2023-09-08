import click
from my_cli.controllers.books_controller import BooksController
from my_cli.controllers.users_controller import UsersController
from my_cli.templates.book_templates import BookTemplates
from my_cli.templates.user_templates import UserTemplates

@click.group()
def cli():
    """Welcome to the Book Library Management System CLI."""
    pass

# Define instances of controllers and templates
books_controller = BooksController()
users_controller = UsersController()
book_templates = BookTemplates()
user_templates = UserTemplates()

# Utility functions for input validation
def validate_year(ctx, param, value):
    """Validate publication year."""
    if value is not None:
        try:
            year = int(value)
            if year < 0:
                raise ValueError("Year cannot be negative")
            return year
        except ValueError:
            raise click.BadParameter("Invalid year. Please enter a valid positive integer.")

def validate_email(ctx, param, value):
    """Validate email address format."""
    if value is not None:
        if "@" not in value or "." not in value:
            raise click.BadParameter("Invalid email address format. Please enter a valid email address.")
    return value

# Add a book
@cli.command()
@click.option('--title', prompt='Title', help='Title of the book', required=True)
@click.option('--author', prompt='Author', help='Author of the book', required=True)
@click.option('--genre', prompt='Genre', help='Genre of the book')
@click.option('--year', prompt='Publication Year', help='Publication year of the book', callback=validate_year)
@click.option('--isbn', prompt='ISBN', help='ISBN of the book', required=True)
def add_book(title, author, genre, year, isbn):
    """Add a new book to the library."""
    try:
        books_controller.add_book(title, author, genre, year, isbn)
        click.echo(f"Added book:\n{book_templates.format_book(title, author, genre, year, isbn)}")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# List all books
@cli.command()
def list_books():
    """List all books in the library."""
    books = books_controller.get_all_books()
    if books:
        for book in books:
            click.echo(book_templates.format_book(
                book['title'], book['author'], book['genre'], book['year'], book['isbn']))
    else:
        click.echo("No books found in the library.")

# Update a book
@cli.command()
@click.option('--isbn', prompt='ISBN', help='ISBN of the book to update', required=True)
@click.option('--title', prompt='New Title', help='New title of the book')
@click.option('--author', prompt='New Author', help='New author of the book')
@click.option('--genre', prompt='New Genre', help='New genre of the book')
@click.option('--year', prompt='New Publication Year', help='New publication year of the book', callback=validate_year)
def update_book(isbn, title, author, genre, year):
    """Update information for a book in the library."""
    try:
        updated_book = books_controller.update_book(isbn, title, author, genre, year)
        if updated_book:
            click.echo(f"Updated book information:\n{book_templates.format_book(**updated_book)}")
        else:
            click.echo(f"Book with ISBN {isbn} not found in the library.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Delete a book
@cli.command()
@click.option('--isbn', prompt='ISBN', help='ISBN of the book to delete', required=True)
def delete_book(isbn):
    """Delete a book from the library."""
    try:
        deleted_book = books_controller.delete_book(isbn)
        if deleted_book:
            click.echo(f"Deleted book:\n{book_templates.format_book(**deleted_book)}")
        else:
            click.echo(f"Book with ISBN {isbn} not found in the library.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Add a user
@cli.command()
@click.option('--username', prompt='Username', help='Username of the user', required=True)
@click.option('--fullname', prompt='Full Name', help='Full name of the user', required=True)
@click.option('--email', prompt='Email', help='Email address of the user', required=True, callback=validate_email)
def add_user(username, fullname, email):
    """Add a new user to the library system."""
    try:
        users_controller.add_user(username, fullname, email)
        click.echo(f"Added user:\n{user_templates.format_user(username, fullname, email)}")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# List all users
@cli.command()
def list_users():
    """List all users in the library system."""
    users = users_controller.get_all_users()
    if users:
        for user in users:
            click.echo(user_templates.format_user(
                user['username'], user['fullname'], user['email']))
    else:
        click.echo("No users found in the library system.")

# Update a user
@cli.command()
@click.option('--username', prompt='Username', help='Username of the user to update', required=True)
@click.option('--fullname', prompt='New Full Name', help='New full name of the user')
@click.option('--email', prompt='New Email', help='New email address of the user', callback=validate_email)
def update_user(username, fullname, email):
    """Update information for a user in the library system."""
    try:
        updated_user = users_controller.update_user(username, fullname, email)
        if updated_user:
            click.echo(f"Updated user information:\n{user_templates.format_user(**updated_user)}")
        else:
            click.echo(f"User with username {username} not found in the library system.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Delete a user
@cli.command()
@click.option('--username', prompt='Username', help='Username of the user to delete', required=True)
def delete_user(username):
    """Delete a user from the library system."""
    try:
        deleted_user = users_controller.delete_user(username)
        if deleted_user:
            click.echo(f"Deleted user:\n{user_templates.format_user(**deleted_user)}")
        else:
            click.echo(f"User with username {username} not found in the library system.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    cli()
