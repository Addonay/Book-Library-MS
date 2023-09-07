class UserTemplates:
    @staticmethod
    def format_user(user):
        """Format a user as a string for display."""
        return f"Username: {user.username}\nFull Name: {user.full_name}\nEmail: {user.email}\nStatus: {'Active' if user.is_active else 'Inactive'}\nAdmin: {'Yes' if user.is_admin else 'No'}"
