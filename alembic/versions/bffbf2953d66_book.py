"""book

Revision ID: bffbf2953d66
Revises: 
Create Date: 2023-09-08 03:46:41.728558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bffbf2953d66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Import SQLAlchemy and create a reference to the Base class and engine
    from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Boolean
    from sqlalchemy.orm import sessionmaker

    # Base = declarative_base()

    # Define the book table
    book = Table(
        'books',
        MetaData(),
        Column('id', Integer, primary_key=True),
        Column('title', String, nullable=False),
        Column('author_id', Integer, ForeignKey('authors.id'), nullable=False),
        Column('genre', String),
        Column('publication_year', Integer),
        Column('isbn', String, unique=True, nullable=False),
        Column('is_available', Boolean, default=True)
    )

    # Bind the engine and create the table
    engine = create_engine('sqlite:///book_lib.db')  # Change this to your database connection URL
    book.create(engine, checkfirst=True)

    # Commit the changes
    connection = engine.connect()
    connection.execute(book)
    connection.close()



def downgrade():
    # Import SQLAlchemy and create a reference to the Base class and engine
    from sqlalchemy import create_engine, MetaData, Table

    # Define the table to drop (in this case, 'books')
    book = Table(
        'books',
        MetaData(),
        autoload=True,  # Load the existing 'books' table metadata
    )

    # Bind the engine and drop the table
    engine = create_engine('sqlite:///book_lib.db')  # Change this to your database connection URL
    book.drop(engine, checkfirst=True)

    # Commit the changes
    connection = engine.connect()
    connection.execute(book)
    connection.close()

