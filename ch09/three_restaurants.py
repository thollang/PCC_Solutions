class Restaurant():
    """A class representing a resaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restraunt(self):
        """Display a summary of the restaurant."""
        msg = "{} serves wonderful {}".format(self.name, self.cuisine_type)
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = "{} is open. Come on in!".format(self.name)
        print("\n" + msg)

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restraunt()


ludvigs = Restaurant("ludvigs's bistro", 'seafood')
ludvigs.describe_restraunt()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restraunt()
