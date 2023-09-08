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

if __name__ == '__main__':
    cli()
