try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another nubmer: ")
    y = int(y)

except:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of {} and {} is {}.".format(x, y, sum))
