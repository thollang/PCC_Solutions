class Restaurant():
    """A class representing a resaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restraunt(self):
        """Display a summary of the restaurant."""
        msg = "{} serves wonderful {}".format(self.name, self.cuisine_type)
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = "{} is open. Come on in!".format(self.name)
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Alow user to increment the number of customers served."""
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""

    def __init__(self, name, cuisine_type = 'ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restraunt()
big_one.show_flavors()