import unittest
from my_cli.controllers.users_controller import UsersController
from my_cli.models.user import User
from my_cli.utils.database import database

class TestUsersController(unittest.TestCase):
    def setUp(self):
        # Initialize the database and controller
        database.create_tables()
        self.users_controller = UsersController()

    def tearDown(self):
        # Clear the database after each test
        with database.get_session() as session:
            session.query(User).delete()

    def test_add_user(self):
        # Test adding a user
        self.users_controller.add_user(
            username="testuser",
            full_name="Test User",
            email="test@example.com"
        )

        # Verify that the user is added to the database
        with database.get_session() as session:
            user = session.query(User).filter_by(username="testuser").first()
            self.assertIsNotNone(user)
            self.assertEqual(user.username, "testuser")
            self.assertEqual(user.full_name, "Test User")
            self.assertEqual(user.email, "test@example.com")

    def test_get_user_by_username(self):
        # Add a test user to the database
        with database.get_session() as session:
            test_user = User(
                username="testuser",
                full_name="Test User",
                email="test@example.com"
            )
            session.add(test_user)

        # Test retrieving the added user by username
        found_user = self.users_controller.get_user_by_username("testuser")
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, "testuser")

if __name__ == '__main__':
    unittest.main()
