from my_cli.models.user import User
from my_cli.utils.database import database

class UsersController:
    def add_user(self, username, full_name, email):
        # Create a new user instance
        new_user = User(
            username=username,
            full_name=full_name,
            email=email
        )

        # Add the user to the database
        with database.get_session() as session:
            session.add(new_user)
            session.commit()

    def get_user_by_username(self, username):
        # Retrieve a user by username from the database
        with database.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            return user
