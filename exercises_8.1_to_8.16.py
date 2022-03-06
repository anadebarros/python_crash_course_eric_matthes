#8.1
def display_message():
  print("I'm learning python")

display_message()

#8.2
def favorite_book(book):
  print(f"One of my favorite books is {book.title()}")

favorite_book("perfume")

#8.3
def make_shirt(size, message):
  print(f"This shirt is size {size} and has '{message}' printed on it.")

make_shirt("M", "yo yo yo what??")
make_shirt(size= "M", message= "what's up")

#8.4
def make_shirt(size= "L", message= "I love python"):
  print(f"This shirt is size {size} and has '{message}' printed on it.")

make_shirt()
make_shirt("M")
make_shirt(message= "whatevs")

#8.5
def describe_city(city, country= "Portugal"):
  print(f"{city.title()} is in {country}")

describe_city("lisbon")
describe_city("porto")
describe_city("tokyo")

