"""Create the class "Restaurant" """

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('\nThe resturant name is '+self.restaurant_name.title())
        print('It\'s of cuisine type '+self.cuisine_type.title())

"""
Initialize attributes of the parent class.
Then initialize attributes specific to an IceCreamStand.
"""

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavour='vanilla'):
        super().__init__(restaurant_name,cuisine_type)
        self.flavour = flavour

    def display_flavour(self):
        print('The available flavour in this restaurant is : ' +self.flavour.title())
           

restaurant1 = Restaurant('alapan', 'vegetarian') 
restaurant1.describe_restaurant()

new_stand1 = IceCreamStand('arsalan','moghal','vanilla')
new_stand1.describe_restaurant()
new_stand1.display_flavour()
