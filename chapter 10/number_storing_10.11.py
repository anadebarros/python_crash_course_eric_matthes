# 10.11
import json

filename = "favorite_number.json"

try:
    number = int(input("What's your favorite number?"))
    with open(filename, mode="w") as my_file:
        json.dump(number, my_file)
except ValueError:
    print("please enter a number")

