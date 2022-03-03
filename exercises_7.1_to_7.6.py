#7.1
car = input("what kind of car would you like to rent?\n")

print(f"Let me see if I can find you a {car}")

#7.2
number_people = input("How many people are in your dinner group?\n")

if int(number_people) > 8:
  print("Sorry you'll have to wait for a table")
else:
  print("Your table is ready")

#7.3
number = input("Gimme a number: ")

if int(number) % 10 == 0:
  print("Your number is a multiple of 10")
else:
  print("Your number is not a multiple of 10")

#7.4
#In this exercise I went a bit further and did not want to keep repeating the input, so added it out of the loop only.
#Then wanted to add additional message before the customer could add an ingredient
#Also wanted my ingredients, but not the word "quit" to be stored in an empty list
#Made sure the program took input well, irrespective of the use of upper or lower case
#Wanted to display a message with all the ingredients in the pizza when the costumer finished
#Also made sure that if the first word was quit, the user had a personalized goodbye message (without displaying the message shown for when they add ingredients)

ingredients = []
print("Please enter a pizza topping")
print("\n(type quit when you wish to stop): ")

while True:
  message = input()
  if message.lower() != "quit":
    ingredients.append(message)
    print(f"I'll add {message} to your pizza.")
    print("\nEnter another toping: ")
  elif message.lower() == "quit" and len(ingredients) != 0:
    print(f"\nNice one! Your pizza with:")
    for ingredient in ingredients:
      print (f"\t{ingredient}")
    print("is on the way!")
    break
  else:
    if message.lower() == "quit" and len(ingredients) == 0:
      print("Byeee!")
      break
#7.5
prompt = "Hi, what is your age? "

while True:
  message = input(prompt)
  if int(message) <=3:
    print("Your entry is free!")
  elif int(message) <=12:
    print("Your ticket is 10$")    
  else:
    print("Your ticket is 15$")
  break

#7.6
prompt = "Hi, what is your age? "
value = True

while value:
  message = input(prompt)
  if int(message) <=3:
    print("Your entry is free!")
    value = False  
  else:
    print("You'll need money!")
    value = False