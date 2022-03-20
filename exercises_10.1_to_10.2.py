# 10.1
filename = "learning_python.txt"

try:
    with open(filename) as my_file:
        text = my_file.read()
        print(text)
except FileNotFoundError as err:
    print("This file was not found")
    raise err

try:
    with open(filename) as my_file:
        text = my_file.readlines()
        for word in text:
            print(word.strip())
except FileNotFoundError as err:
    print("This file was not found")
    raise err


try:
    with open(filename) as my_file:
        text = my_file.readlines()
except FileNotFoundError as err:
    print("This file was not found")
    raise err

sentence = ""
for word in text:
    sentence += word

print(sentence)

# 10.2

try:
    with open(filename) as my_file:
        text = my_file.read()
        new_text = text.replace("Python", "Ruby")
        print(new_text)
except FileNotFoundError as err:
    print("This file was not found")
    raise err

# 10.3
name = input("Please tell me your name: ")

try:
    with open("guest.txt", mode="w") as my_file:
        my_file.write(name)
except FileNotFoundError as err:
    print("Your file could not be found")
    raise err

# 10.4
print("Enter 'exit' when you are finished.")
while True:
    name2 = input("Please tell me your name: ")
    if name2 == "exit".lower():
        break
    else:
        with open("guest_book.txt", mode="a") as my_file:
            my_file.write(name2 + "\n")
        print(f"Welcome {name2}!")

# 10.5

responses = []

while True:
    answer = input("Why do you like programming? ")
    responses.append(answer)

    quit = input("Would you like to quit? Y/N ")
    if quit == "Y".lower():
        break


with open("poll.txt", mode="a") as my_file:
    for response in responses:
        my_file.write(response + "\n")
