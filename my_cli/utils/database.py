from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///book_lib.db" 

# Create a base class for declarative models
Base = declarative_base()

class Database:
    """
    A class for managing database connections and sessions.

    Attributes:
        engine: The SQLAlchemy database engine.
        session_local: A session factory for creating database sessions.
    """

    def __init__(self):
        """
        Initializes the Database class by creating a database engine and session factory.
        """
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        """
        Creates database tables based on the declarative models.
        """
        Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        """
        Creates and returns a new database session.

        Returns:
            A SQLAlchemy database session.
        """
        return self.SessionLocal()

    def close_session(self, session):
        """
        Closes the provided database session.

        Args:
            session: The database session to close.
        """
        session.close()

database = Database()
database.create_tables()
print("Database tables have been created")
