#5.3
alien_color = "green"

if alien_color == "green":
  print("You just earned 5 points")

if alien_color == "red":
  print("oops")

#5.4
alien_color = "red"

if alien_color == "green":
  print("congrats, you won 5 points for shooting the beast!")
else:
  print("You just won 10 points!")

#5.5
if alien_color == "green":
  print("congrats, you won 5 points for shooting the beast!")
elif alien_color == "yellow":
  print("you earned 10 points")
else:
  print("you earned 15 points")

#5.6
age = 38

if age < 2:
  print("you're a baby")
elif age < 4:
  print("you're toddler")
elif age < 13:
  print("you're a kid")
elif age < 20:
  print("you're a teenager")
elif age < 65:
  print("you're an adult")
else:
  print("you're an elder")

#5.7
favorite_fruits = ["strawberry", "tangerines", "pomegranate",]

if "apple" in favorite_fruits:
  print("You really like apples")

if "strawberry" in favorite_fruits:
  print("You really like strawberries")

if "coconut" in favorite_fruits:
  print("You really like coconuts")

if "tangerines" in favorite_fruits:
  print("You really like tangerines")

if "pomegranate" in favorite_fruits:
  print("You really like pomegranate")

#5.8 and 5.9
usernames = ["admin", "joe123", "gumi_manuli", "rocket-ana", "birdy_nom_nom"]

if usernames:
  for username in usernames:
    if username == "admin":
      print(f"Welcome back {username}, would you like to see a report?")
    else:
      print(f"Hello {username}, nice to see you again")
else:
  print("we need to find some users first")

#5.10
current_users = ["joe123", "gumi_manuli", "rocket-ana", "birdy_nom_nom", "ellie"]

new_users = ["ELlie", "Gumi_Manuli", "elton", "Steven", "gugugu"]

for user in new_users:
  if user.lower() in current_users:
    print(f"{user} you need a new username")
  else:
    print(f"{user} that username is available")

#5.11
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
  if number <= 1:
    print(f"{number}st\n")
  elif number <= 2:
    print(f"{number}nd\n")
  elif number <= 3:
    print(f"{number}rd\n")
  else:
    print(f"{number}th\n")