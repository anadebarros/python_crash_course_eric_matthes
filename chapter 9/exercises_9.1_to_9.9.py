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
            f"My first name is {self.first_name} "
            f"and my last name is {self.last_name}."
            f"I'm {self.age} years old and I like {self.interests}"
        )

    def greet_user(self):
        print(f"Hi {self.first_name}! Welcome!")


user1 = User(input(), "bonanza", 40, sports=True, reading=False)
user2 = User(input(), "marques", 32, sports=True, reading=True)
user3 = User(input(), "banana", 38, sports=True, reading=False)

print(user1.describe_user(), user1.greet_user())
print(user2.describe_user(), user2.greet_user())
print(user3.describe_user(), user3.greet_user())


# 9.4


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

# 9.5


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

# 9.6


class Restaurant():

    status = "open"

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"This restaurant is called {self.name}"
            f" and it cooks {self.cuisine_type} food"
        )

    def open_restaurant(self):
        print(f"This restaurant is {self.status}")

    def set_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def ice_cream_flavors(self, *flavors):
        for self.flavor in flavors:
            self.flavors.append(self.flavor)

        print("You have chosen an ice cream with: ")
        for self.flavor in self.flavors:
            print("-" + self.flavor)


ice_cream_stand = IceCreamStand('popone', 'gelataria')

ice_cream_stand.ice_cream_flavors('baunilha', 'morango')

# 9.7


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


class Admin(User):

    def __init__(self, first_name, last_name, age):

        super().__init__(first_name, last_name, age)
        self.privileges = ['add post', 'delete post', 'be user']


def show_privileges(self):
    print('By being an admin you can: ')
    for self.privilege in self.privileges:
        print(f'- {self.privilege}')


admin = Admin('ana', 'barros', 38)

admin.show_privileges()

# 9.8


class Admin(User):

    def __init__(self, first_name, last_name, age):

        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):

        print('By being an admin you can: ')
        if self.privileges:
            for self.privilege in self.privileges:
                print(f'- {self.privilege}')
        else:
            print('You do not have priviledges')


admin = Admin('ana', 'barros', 38)

admin.privileges.show_privileges()

admin.privileges.privileges = ['add', 'delete', 'modify']

admin.privileges.show_privileges()

# 9.9


class Car():

    def __init__(self, manufacturer, model, year):

        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):

        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):

        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=60):

        self.battery_size = battery_size

    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):

        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size <= 85:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


tesla = ElectricCar('Tesla', 'qwex', 2020)

tesla.battery.get_range()

tesla.battery.upgrade_battery()

tesla.battery.get_range()
