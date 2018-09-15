class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('\nThe resturant name is '+self.restaurant_name.title())
        print('It\'s of cuisine type '+self.cuisine_type.title() + '\n')
        
    def set_number_served(self,number):
        self.number_served = number
        print('The number of person served '+ str(self.number_served))

    def increment_number_served(self,num):
        if num >= self.number_served:
            self.number_served += num
            print('The number of person served '+ str(self.number_served))
        else:
            print("Don't try to be oversmart and you can't change the served number")

"""Create the instance of class "Restaurant" and assign it to a variable "restaurant1" """

restaurant1 = Restaurant('alapan', 'vegetarian') 
restaurant1.describe_restaurant()

restaurant1.set_number_served(23)
restaurant1.increment_number_served(30)

restaurant1.increment_number_served(20)
