from random import randint

from collections import OrderedDict


new_dict = OrderedDict()

new_dict['name'] = ['gumi']
new_dict['age'] = [9]
new_dict['color'] = ['yellow']

for key, value in new_dict.items():
    print(f"{key} {value}\n")


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die1 = Die()

results = []
for roll_num in range(6):
    result = die1.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

die2 = Die(10)

results = []
for roll_num in range(10):
    result = die2.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)

die3 = Die(20)

results = []
for roll_num in range(20):
    result = die2.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
print(results)
