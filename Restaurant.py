class Restaurant:
    """Simple code For Restaurant"""

    def __init__(self,restaurant_name,cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 5

    def describe_restaurant(self):
        print(f"The Restaurant is {self.restaurant_name}.")
        print(f"\t Cusine Type : {self.cusine_type}.")

    def set_served_numbers(self):
        print(f"This Restaurant has served to {self.number_served} customers ")

    def increment_number_served(self,number):
        print(f"Update Of Served Customer : {number}")
        self.number_served += number

    def open_restaurant(self):
        print("------Restaurant is Open------")

restaurant = Restaurant('Rasraj','All Indian Dishes')
restaurant.describe_restaurant()
print("__"*40)
restaurant = Restaurant('Shanghai Club','Chinese Food')
restaurant.describe_restaurant()
print("--"*40)
restaurant = Restaurant('Thepla House','Gujrati')
restaurant.describe_restaurant()
print("--"*40)
restaurant = Restaurant('Dhaba','Punjabi food')
restaurant.describe_restaurant()
print("--"*40)
restaurant.increment_number_served(5)
restaurant.set_served_numbers()

restaurant.increment_number_served(7)
restaurant.set_served_numbers()

restaurant.increment_number_served(8)
restaurant.set_served_numbers()



