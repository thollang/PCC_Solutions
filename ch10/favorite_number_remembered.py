import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favourite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thank's I'll remember that.")
else:
    print("I know your favorite number! It's {} ".format(number))
