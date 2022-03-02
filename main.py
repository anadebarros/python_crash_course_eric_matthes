#6.7
person_1 = {
  'first_name':'Golias',
  'last_name': 'Manuel',
  'age': 9,
  'city': 'lisboa',  
}

person_2 = {
  'first_name':'Ginja',
  'last_name': 'Maria',
  'age': 14,
  'city': 'lisboa',  
}

person_3 = {
  'first_name':'Didi',
  'last_name': 'Anne',
  'age': 13,
  'city': 'Porto de Mós',  
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"This cutie's first name is {person['first_name']}, last name is {person['last_name']} age is {person['age']} and city is {person['city']}\n"
         )

#6.8
gumi = {
  'species':'dog',
  'owner': 'Ana',
}

ginja = {
  'species':'dog',
  'owner': 'Mariana',
}

didi = {
  'species':'cat',
  'owner': 'Marina',  
}

pets = [gumi, ginja, didi]

for animal in pets:
  print(
    f"This cutie's species is {animal['species']}, and its owner is {animal['owner']}\n"
  )
  
#6.9
favorite_places = {
  'Ana': ['Tokyo', 'Lisbon', 'Los Angeles'],
  'Marina': ['Kyoto', 'Paris', 'Algarve'],
  'Gumi': ['margem sul', 'praia', 'ferreira do zêzere'],
}

for people, places in favorite_places.items():
  print(f"{people}'s favorites places are:\n")
  for place in places:
    print(f"\t {place}\n")

#6.10
people = {
  'Ana': [3, 0],
  'Marina': [9, 6],
  'Gumi' : [4, 5, 6],
  'Rafa': [6, 2],
}

#6.11

cities = {
  'lisbon': {
    'country': 'portugal',
    'population': 1100000,
    'fact': 'beautiful',
  },
  'new york': {
    'country': 'united states',
    'population': 13000000,
    'fact': 'cold',
  },
  'tokyo': {
    'country': 'japan',
    'population': 15000000,
    'fact': 'kawaii',
  },
}

for city, city_info in cities.items():
  country = city_info['country']
  population = city_info['population']
  fact = city_info['fact']
  print(f"{city.title()} is located in {country}, has a population of {population} and is {fact}\n")
