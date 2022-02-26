#4.3
for number in range(1,21):
  print(number)

#4.4
million_numbers = list(range(1,1000001))

for number in million_numbers:
  print(number)

#4.5
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

#4.6
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
  print(number)

#4.7
multiples_of_three = list(range(3,21,3))
for number in multiples_of_three:
  print(number)
#alternatively we could also do it like this
multiples_of_three = []
for number in range(3,21,3):
  multiples_of_three.append(number)
  print(number)
  

#4.8
cubes = []

for number in range(1,11):
  cubes.append(number**3)

for number in cubes:
  print(number)

#4.9
cubes = [number**3 for number in range (1,11)]
print(cubes)