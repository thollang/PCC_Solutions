def make_sandwich(*items):
    """Make a sandwwich with the given items."""
    print("\nI'll make a great sandwich:")
    for item in items:
        print("  ...adding [{}] to your sandwich.".format(item))
    print("Your sandwich is ready!")


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanu butter', 'strawberry jam')
