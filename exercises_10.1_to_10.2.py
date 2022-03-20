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
