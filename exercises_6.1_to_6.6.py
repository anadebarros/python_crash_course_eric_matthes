#6.1
person = {
  "first_name":"Golias",
  "last_name": "Manuel",
  "age": 9,
  "city": "lisboa",  
}

print(person["first_name"], 
      person["last_name"], 
      person["age"], 

      person["city"])
#6.2
people = {
  "Ana": 3,
  "Marina": 9,
  "Gumi" : 4,
  "Rafa": 6,
}

print("Ana's favorite number is " + str(people["Ana"]))

print(f"Marina's favorite number is {people['Marina']}")

#6.3
glossary = {
  'variable': 'is something that keeps a value',
  'string' : 'is a group of letters and sentences',
  'float': 'is a decimal number',
}

print(f"A variable {glossary['variable']}\n")

print(f"A string {glossary['string']}\n")

#6.4
glossary = {
  'variable': 'is something that keeps a value',
  'string' : 'is a group of letters and sentences',
  'float': 'is a decimal number',
}

for key, value in glossary.items():
  print(f"A {key} {value}\n")

#6.5
rivers = {
  'nile': 'egypt',
  'douro': 'portugal',
  'athabasca': 'canada',
}

for key, value in rivers.items():
  print(f"The {key.title()} is a river that runs through {value.title()}. \n")

for river in rivers.keys():
  print(river.title())

for country in rivers.values():
  print(country.title())

#6.6
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

should_take_poll = ['jen', 'john', 'edward', 'anthony']

for name in favorite_languages:
  if name in should_take_poll:
    print(f"Thank you {name.title()} for taking the poll.\n")
  else:
    print(f"{name.title()} we invite you to take the poll.\n")
