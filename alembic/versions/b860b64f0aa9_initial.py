"""initial

Revision ID: b860b64f0aa9
Revises: 
Create Date: 2023-09-11 01:55:37.699445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b860b64f0aa9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a 'books' table
    op.create_table(
        'books',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('author', sa.String(), nullable=False),
        sa.Column('genre', sa.String(), nullable=True),
        sa.Column('publication_year', sa.Integer(), nullable=True),
        sa.Column('isbn', sa.String(), unique=True, nullable=False),
        sa.Column('is_available', sa.Boolean(), default=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create an 'authors' table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('is_admin', sa.Boolean(), server_default='false'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    # Drop the 'books' and 'authors' tables
    op.drop_table('books')
    op.drop_table('users')
