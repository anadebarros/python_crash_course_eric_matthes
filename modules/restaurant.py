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
