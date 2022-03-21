filename = "course_material/chapter_10/pi_million_digits.txt"

try:
    with open(filename) as my_file:
        lines = my_file.readlines()
except FileNotFoundError as err:
    print("Sorry, file not found")
    raise err

pi_string = " "

for line in lines:
    pi_string += line.rstrip()

birthday = input("Please enter your birthday in the ddmmyy format: ")

if birthday in pi_string:
    print("Your birthday is in the first million digits of pi!")
else:
    print("Your bday is not in the first million digits of pi")
