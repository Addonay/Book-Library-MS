"""user

Revision ID: af6c043fa007
Revises: bffbf2953d66
Create Date: 2023-09-08 03:54:30.653153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af6c043fa007'
down_revision = 'bffbf2953d66'
branch_labels = None
depends_on = None


def upgrade():
    # Import SQLAlchemy and create a reference to the Base class and engine
    from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

    # Base = declarative_base()

    # Define the user table
    user = Table(
        'users',
        MetaData(),
        Column('id', Integer, primary_key=True),
        Column('username', String, nullable=False, unique=True),
        Column('fullname', String, nullable=False),
        Column('email', String, nullable=False, unique=True)
    )

    # Bind the engine and create the table
    engine = create_engine('sqlite:///book_lib.db')  # Change this to your database connection URL
    user.create(engine, checkfirst=True)

    # Commit the changes
    connection = engine.connect()
    connection.execute(user)
    connection.close()



def downgrade():
    # Import SQLAlchemy and create a reference to the Base class and engine
    from sqlalchemy import create_engine, MetaData, Table

    # Define the table to drop (in this case, 'users')
    user = Table(
        'users',
        MetaData(),
        autoload=True,  # Load the existing 'users' table metadata
    )

    # Bind the engine and drop the table
    engine = create_engine('sqlite:///book_lib.db')  # Change this to your database connection URL
    user.drop(engine, checkfirst=True)

    # Commit the changes
    connection = engine.connect()
    connection.execute(user)
    connection.close()

