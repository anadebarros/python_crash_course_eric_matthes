# 9.1
class Restaurant():

    status = "open"

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"This restaurant is called {self.name} and"
            "it cooks {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"This restaurant is {self.status}")


restaurant = Restaurant("Cucu", "Indian")
print(restaurant.name)
print(restaurant.cuisine_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

# 9.2
restaurant1 = Restaurant("Chicken n frens", "Grill")
restaurant2 = Restaurant("Comaki", "Traditional Food")
restaurant3 = Restaurant("General Ping", "Chinese")

print(restaurant1.describe_restaurant())
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant())

# 9.3


class User():

    def __init__(self, first_name, last_name, age, **interests):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.interests = interests

    def describe_user(self):

        print(
            f"My first name is {self.first_name} and my last name"
            "is {self.last_name}. I'm {self.age} years old"
            "and I like {self.interests}")

    def greet_user(self):
        print(f"Hi {self.first_name}! Welcome!")


user1 = User(input(), "bonanza", 40, sports=True, reading=False)
user2 = User(input(), "marques", 32, sports=True, reading=True)
user3 = User(input(), "banana", 38, sports=True, reading=False)

print(user1.describe_user(), user1.greet_user())
print(user2.describe_user(), user2.greet_user())
print(user3.describe_user(), user3.greet_user())


9.4


class Restaurant():

    status = "open"

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"This restaurant is called {self.name} and"
            "it cooks {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"This restaurant is {self.status}")

    def set_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('chimkens', 'grill')
print(restaurant.number_served)

restaurant.number_served = 15
print(restaurant.number_served)

restaurant.set_number_served(30)

print(restaurant.number_served)

9.5


class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Ana', 'Barros', 38)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)
