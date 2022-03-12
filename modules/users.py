class User():

    def __init__(self, first_name, last_name, age, **interests):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.interests = interests
        self.login_attempts = 0

    def describe_user(self):

        print(
            f"My first name is {self.first_name} "
            f"and my last name is {self.last_name}."
            f"I'm {self.age} years old and I like {self.interests}"
        )

    def greet_user(self):
        print(f"Hi {self.first_name}! Welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, age):

        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


def show_privileges(self):
    print('By being an admin you can: ')
    for self.privilege in self.privileges:
        print(f'- {self.privilege}')


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
