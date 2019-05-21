class Restaurant():
    """A class representing a resaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
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


#resaurant = Restaurant('the mean queen', 'pizza')
#resaurant.describe_restraunt()
#
#print("\nNumber served: {}".format(str(resaurant.number_served)))
#resaurant.number_served = 430
#print("\nNumber served: {}".format(str(resaurant.number_served)))
#
#resaurant.set_number_served(1257)
#print("\nNumber served: {}".format(str(resaurant.number_served)))
#
#resaurant.increment_number_served(239)
#print("\nNumber served: {}".format(str(resaurant.number_served)))
