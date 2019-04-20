favourite_pizzas=['pepperoni','hawaiian','veggie']
#create a copy with slices
friend_pizzas=favourite_pizzas[:]

favourite_pizzas.append("meat lover's")
friend_pizzas.append("pesto")

print("My favourite pizzas are:")
for pizza in favourite_pizzas:
    print(pizza)

print("My friend pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
