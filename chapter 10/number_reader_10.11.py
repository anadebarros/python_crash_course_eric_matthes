import json

filename = "favorite_number.json"

with open(filename) as my_file:
    favorite_number = json.load(my_file)
    print(favorite_number)
