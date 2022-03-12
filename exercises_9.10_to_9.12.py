# 9.10 and 9.11
from modules.restaurant import Restaurant, IceCreamStand

from modules.users import Admin

new_restaurant = Restaurant('Chicken and Frens', 'Grilled chicken')

new_restaurant.describe_restaurant()

new_restaurant.set_number_served(13)

print(new_restaurant.number_served)

new_ice_cream = IceCreamStand('Fresquinho', 'gelataria')

new_ice_cream.ice_cream_flavors('morango', 'baunilha', 'chocolate')


ana = Admin('ana', 'de Barros', 38)

ana.privileges.privileges = ['delete', 'add', 'modify']

ana.privileges.show_privileges()
