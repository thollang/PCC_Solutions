from random import randint


class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialized the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)


d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-sided die:")
print(results)

d10 = Die(sides=10)
for roll_num in range(10):
    result = d10.roll_die()
    results.append((result))

print("10 rolls of a 10-sided die:")
print(results)
