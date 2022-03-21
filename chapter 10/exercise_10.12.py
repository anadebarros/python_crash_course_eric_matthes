import json

filename = "favorite_number.json"

while True:
    try:
        with open(filename) as my_file:
            favorite_number = json.load(my_file)
    except FileNotFoundError:
        number = int(input("What's your favorite number?"))
        with open(filename, mode="w") as my_file:
            json.dump(number, my_file)
    except ValueError:
        print("please enter a number")
    else:
        print(favorite_number)
        print("this is working")
        break
