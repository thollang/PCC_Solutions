class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information"""
        print("\n  {} {}.".format(self.first_name, self.last_name))
        print("  Username: {}".format(self.username))
        print("  Email: {}".format(self.email))
        print("  Location: {}".format((self.location)))

    def greet_user(self):
        """Display a personalized greeting to user."""
        print("\nWelcome back, {}!".format(self.username))

eric = User('eric', 'matthes', 'e_matthes', 'e_mattes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()