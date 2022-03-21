# 10.6 and 10.7
while True:

    try:

        number1 = int(input("Please enter a number: "))

        number2 = int(input("Please enter another number: "))

        sum = number1+number2

    except ValueError:
        print("Please enter a number doofus!")
    else:
        print(sum)
        break

# 10.8

files = ["./chapter 10/cats.txt", "./chapter 10/dogs.txt"]

try:
    for file in files:
        with open(file) as my_file:
            names = my_file.read()
            print(names + "\n")
except FileNotFoundError:
    print("Sorry, file not found")

# 10.10

filename = "./chapter 10/xmas_carol.txt"


def CountThe(file):
    try:
        with open(file) as my_file:
            text = my_file.read()
            times_appears = text.lower().count("the")
    except FileNotFoundError:
        print("Sorry file not found")
    else:
        print(times_appears)


print(CountThe(filename))
