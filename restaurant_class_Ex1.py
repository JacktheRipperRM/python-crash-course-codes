class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('\nThe resturant name is '+self.restaurant_name.title())
        print('It\'s of cuisine type '+self.cuisine_type.title())

    def open_restaurant(self):
        print('\nWelcome to the '+self.restaurant_name.title()+ ' restaurant')
        print('You can get '+self.cuisine_type.title()+ " food here.")


restaurant1 = Restaurant('chilli\'s','chinese')
restaurant2 = Restaurant('alishan','mughal')

restaurant1.open_restaurant() 
restaurant1.describe_restaurant()
     
restaurant2.open_restaurant() 
restaurant2.describe_restaurant()
    
