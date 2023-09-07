# Book Library Management System CLI

A command-line interface (CLI) application for managing a book library. This CLI allows you to add, search for books, and manage user information in your library system.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Adding a Book](#adding-a-book)
  - [Searching for a Book](#searching-for-a-book)
  - [Adding a User](#adding-a-user)
  - [Logging In As A User](logging-in-as-a-user)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 or higher installed on your system.
- Pipenv for managing your project's virtual environment (if you prefer).

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Addonay/book-library-cli.git
   ```

2. Navigate to the project directory:

   ```sh
   cd book-library-cli
   ```

3. Install project dependencies (using Pipenv or your preferred method):

   ```sh
   pipenv install
   ```

## Usage

To use the Book Library Management System CLI, follow these instructions for different commands:

### Adding a Book

To add a new book to the library, use the following command:

```sh
pipenv run python my_cli/cli.py add_book
```

Follow the prompts to provide book details, including title, author, genre, publication year, and ISBN.

### Searching for a Book

To search for a book in the library, use the following command:

```sh
pipenv run python my_cli/cli.py search_book
```

Follow the prompts to enter the title of the book you want to search for. The CLI will display the book's details if it exists in the library.

### Adding a User

To add a new user to the library system, use the following command:

```sh
pipenv run python my_cli/cli.py add_user
```

Provide the user's username, full name, and email address as prompted.
### Logging In As A User
To log into an existing account on the library management system using their credentials, use this command:
```sh
pipenv run python my_cli/cli.py login --username <USERNAME>  --password <<PASSWORD>>
```
The password will be hashed before it is stored so that no plain text passwords are saved anywhere!

# LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
