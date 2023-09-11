from my_cli.models.user import User
from my_cli.utils.database import database

class UsersController:
    def add_user(self, username, full_name, email, password):
        # Create a new user instance
        new_user = User(
            username=username,
            full_name=full_name,
            email=email,
            password=password
        )

        # Add the user to the database
        with database.get_session() as session:
            session.add(new_user)
            session.commit()

    def get_user_by_username(self, username):
        # Retrieve a user by username from the database
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            return user  # Returns the user instance or None if not found

    def get_all_users(self):
        # Retrieve all users from the database
        with database.get_session() as session:
            users = session.query(User).all()
            return users  # Returns a list of user instances or an empty list if no users found

    def delete_user(self, username):
        # Delete a user by username from the database
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user:
                session.delete(user)
                session.commit()
                return user  # Returns the deleted user instance
            else:
                return None  # User not found, return None

    def update_user(self, username, full_name=None, email=None):
        # Update user information by username in the database
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user:
                if full_name is not None:
                    user.full_name = full_name
                if email is not None:
                    user.email = email
                session.commit()
                return user  # Returns the updated user instance
            else:
                return None  # User not found, return None
            
    def get_user_password(self, username):
        """Get the stored password for a user by their username."""
        # Replace 'your_session' with the actual SQLAlchemy session instance
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user:
                return user.password
            else:
                raise Exception("User not found")
            
    def is_admin(self, username):
        """
        Check if a user is an admin.

        Args:
            username (str): The username of the user to check.

        Returns:
            bool: True if the user is an admin, False otherwise.
        """
        # Assuming you have a User model with an 'is_admin' field
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user:
                return user.is_admin
            return False

    def verify_user(self, username, password):
        """
        Verify a user's username and password.

        Args:
            username (str): The username of the user to verify.
            password (str): The password to verify.

        Returns:
            bool: True if the username and password match, False otherwise.
        """
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user and user.password == password:
                return True
            return False