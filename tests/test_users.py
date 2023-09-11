import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.database import Base
from models.user import User 

# Create an SQLite in-memory database for testing
DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database schema
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Create a new database session for each test."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_create_user(db_session):
    """Test creating a new user."""
    user_data = {
        "username": "testuser",
        "full_name": "Test User",
        "email": "test@example.com",
        "password": "testpassword", 
        "is_active": True,
        "is_admin": False,
    }
    user = User(**user_data)
    db_session.add(user)
    db_session.commit()

    assert user.id is not None
    assert user.username == "testuser"
    assert user.full_name == "Test User"
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.is_admin is False

def test_update_user(db_session):
    """Test updating a user's information."""
    # Create a user
    user_data = {
        "username": "updateuser",
        "full_name": "Update User",
        "email": "update@example.com",
        "password": "updatepassword",
        "is_active": True,
        "is_admin": False,
    }
    user = User(**user_data)
    db_session.add(user)
    db_session.commit()

    # Update the user's information
    updated_data = {
        "full_name": "Updated User Name",
        "email": "updated@example.com",
    }
    db_session.query(User).filter(User.id == user.id).update(updated_data)
    db_session.commit()

    # Retrieve the updated user from the database
    updated_user = db_session.query(User).filter(User.id == user.id).first()

    assert updated_user.full_name == "Updated User Name"
    assert updated_user.email == "updated@example.com"

def test_delete_user(db_session):
    """Test deleting a user."""
    # Create a user
    user_data = {
        "username": "deleteuser",
        "full_name": "Delete User",
        "email": "delete@example.com",
        "password": "deletepassword",
        "is_active": True,
        "is_admin": False,
    }
    user = User(**user_data)
    db_session.add(user)
    db_session.commit()

    # Delete the user
    db_session.delete(user)
    db_session.commit()

    # Attempt to retrieve the deleted user
    deleted_user = db_session.query(User).filter(User.id == user.id).first()

    assert deleted_user is None
