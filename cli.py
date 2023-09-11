import click
import tabulate
from my_cli.controllers.books_controller import BooksController
from my_cli.controllers.users_controller import UsersController

# Define a common function for formatting tables
def format_table(data, headers):
    tablefmt = "grid"  # Customize the table format (e.g., "grid", "pretty", "fancy_grid", etc.)

    # Customize cell value formatting (e.g., align numbers to the right)
    table = tabulate.tabulate(data, headers=headers, tablefmt=tablefmt, numalign="right")
    
    return table

# Define instances of controllers and templates
books_controller = BooksController()
users_controller = UsersController()

@click.group()
def cli():
    """Welcome to the Book Library Management System CLI."""
    pass

# Utility functions for input validation
# def validate_year(value):
#     """Validate publication year."""
#     if value is not None:
#         try:
#             year = int(value)
#             if year < 0:
#                 raise ValueError("Year cannot be negative")
#             return year
#         except ValueError:
#             raise click.BadParameter("Invalid year. Please enter a valid positive integer.")

# def validate_email(value):
#     """Validate email address format."""
#     if value is not None:
#         if "@" not in value or "." not in value:
#             raise click.BadParameter("Invalid email address format. Please enter a valid email address.")
#     return value

# Add a book
@cli.command()
@click.option('--title', prompt='Title', help='Title of the book', required=True)
@click.option('--author', prompt='Author', help='Author of the book', required=True)
@click.option('--genre', prompt='Genre', help='Genre of the book')
@click.option('--year', prompt='Publication Year', help='Publication year of the book')
@click.option('--isbn', prompt='ISBN', help='ISBN of the book', required=True)
@click.option('--username', prompt='Username', help='Your username', required=True)
@click.option('--password', prompt='Password', help='Your password', hide_input=True, required=True)
def add_book(title, author, genre, year, isbn, username, password):
    """Add a new book to the library."""
    try:
         # Check if the user is an admin. You need to implement this logic in UsersController.
        if users_controller.is_admin(username):
            # Verify the user's username and password
            if users_controller.verify_user(username, password):
                new_book = books_controller.add_book(title, author, genre, year, isbn)
                click.echo(f"Book '{new_book}' added successfully.")
            else:
                click.echo("Invalid username or password. You are not authorized to add a book.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# List all books
@cli.command()
def list_books():
    """List all books in the library."""
    books = books_controller.get_all_books()
    if books:
        table_data = [{"Title": book.title, "Author": book.author, "Genre": book.genre, "Year": book.publication_year, "ISBN": book.isbn} for book in books]
        table = tabulate.tabulate(table_data, headers="keys", tablefmt="pretty")
        click.echo(table)
    else:
        click.echo("No books found in the library.")


# Update a book
@cli.command()
@click.option('--isbn', prompt='ISBN', help='ISBN of the book to update', required=True)
@click.option('--title', prompt='New Title', help='New title of the book')
@click.option('--author', prompt='New Author', help='New author of the book')
@click.option('--genre', prompt='New Genre', help='New genre of the book')
@click.option('--year', prompt='New Publication Year', help='New publication year of the book')
def update_book(isbn, title, author, genre, year):
    """Update information for a book in the library."""
    try:
        updated_book = books_controller.update_book(isbn, title, author, genre, year)
        click.echo(f"Book '{updated_book}' updated successfully.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Delete a book
@cli.command()
@click.option('--title', prompt='Title', help='Title of the book to delete', required=True)
@click.option('--username', prompt='Username', help='Your username', required=True)
@click.option('--password', prompt='Password', help='Your password', hide_input=True, required=True)
def delete_book(title, username, password):
    """Delete a book from the library."""
    try:
        # Check if the user is an admin. You need to implement this logic in UsersController.
        if users_controller.is_admin(username):
            # Verify the user's username and password
            if users_controller.verify_user(username, password):
                books_controller.delete_book(title)
                click.echo(f"Book '{title}' deleted successfully.")
            else:
                click.echo("Invalid username or password. You are not authorized to delete the book.")
        else:
            click.echo("You are not authorized to delete books. Only admins can perform this action.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Add a user
@cli.command()
@click.option('--username', prompt='Username', help='Username of the user', required=True)
@click.option('--fullname', prompt='Full Name', help='Full name of the user', required=True)
@click.option('--email', prompt='Email', help='Email address of the user', required=True)
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='Password for the user', required=True)
def add_user(username, fullname, email, password):
    """Add a new user to the library system."""
    try:
        users_controller.add_user(username, fullname, email, password)
        click.echo(f"User '{username}' added successfully.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")


# List all users
@cli.command()
def list_users():
    """List all users in the library system."""
    users = users_controller.get_all_users()
    if users:
        table_data = [{"Username": user.username, "Full Name": user.full_name, "Email": user.email, "Password": user.password} for user in users]
        table = tabulate.tabulate(table_data, headers="keys", tablefmt="pretty")
        click.echo(table)
    else:
        click.echo("No users found in the library system.")


# Update a user
@cli.command()
@click.option('--username', prompt='Username', help='Username of the user to update', required=True)
@click.option('--fullname', prompt='New Full Name', help='New full name of the user')
@click.option('--email', prompt='New Email', help='New email address of the user')
def update_user(username, fullname, email):
    """Update information for a user in the library system."""
    try:
        updated_user = users_controller.update_user(username, fullname, email)
        click.echo(f"User '{username}' updated successfully to '{updated_user}'.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Delete a user
@cli.command()
@click.option('--username', prompt='Username', help='Username of the user to delete', required=True)
@click.option('--password', prompt='Password', help='Password to verify user identity', hide_input=True, required=True)
def delete_user(username, password):
    """Delete a user from the library system."""
    try:
        # Retrieve the user's stored password from the database based on their username
        stored_password = users_controller.get_user_password(username)
        
        # Check if the entered password matches the stored password
        if password == stored_password:
            users_controller.delete_user(username)
            click.echo(f"User {username} deleted successfully.")
        else:
            click.echo("Error: Password verification failed. User not deleted.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")


if __name__ == '__main__':
    cli()