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
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """A suer with administrative privilegs."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


#eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
#eric.describe_user()
#
#eric.privileges.show_privileges()
#
#eric_privileges = ['can rest passwords',
#                   'can moderate discussions',
#                   'can suspend accounts',
#                   ]
#
#eric.privileges.privileges = eric_privileges
#eric.privileges.show_privileges()
