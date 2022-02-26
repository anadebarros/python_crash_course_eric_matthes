#4.10
list = ["gumi", "marina", "bart", "simpson", 1, 2,3]

print("The first three items in the list are:\n")
print(list[:3])

print("Three items from the middle of the list are:\n")
print(list[2:5])

print("The last three items from the list are:\n")
print(list[-3:])

#4.11
pizzas = ["margarita", "anchovies", "mushroom"]
friend_pizzas = pizzas[:]

pizzas.append("basilica")
friend_pizzas.append("salami")

print("My favorite pizzas are:\n")
for pizza in pizzas:
  print(pizza)

print("My friend's favorite pizzas are:\n")
for pizza in friend_pizzas:
  print(pizza)

#4.12
my_foods = ["pizza", "falafel", "carrot cake"]
for food in my_foods:
  print(food)

friends_food = my_foods[:]
friends_food.append("ice cream")

for food in friends_food:
  print(food)
