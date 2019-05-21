class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information"""
        print("\n  {} {}.".format(self.first_name, self.last_name))
        print("  Username: {}".format(self.username))
        print("  Email: {}".format(self.email))
        print("  Location: {}".format((self.location)))

    def greet_user(self):
        """Display a personalized greeting to user."""
        print("\nWelcome back, {}!".format(self.username))

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_mattes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: {}".format(str(eric.login_attempts)))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: {}".format(str(eric.login_attempts)))
