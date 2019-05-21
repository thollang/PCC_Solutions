class Car():
    """A simple attempt ot represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing hte car's mileage."""
        print("This car has {} miles on it".format(str(self.odometer_reading)))

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amout to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an eletric car."""

    def __init__(self, battery_size=60):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a {} -kWH battery.".format(str(self.battery_size)))

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            ragne = 185

        message = "This car can go approximately {}".format(str(range))
        message += " miles on a full charge."
        print(message)

    def battery_upgrade(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh")
        else:
            print("The battery is already upgraded.")

class ElectricCar(Car):
    """Modles aspects of car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        The initialzie attributes specific to an eletric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.battery_upgrade()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.battery_upgrade()
my_tesla.battery.describe_battery()
