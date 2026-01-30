# #9.1
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"\nНаш ресторан называется {self.restaurant_name.title()}.")
#         print(f"Ресторан специплизируется на {self.cuisine_type}.")

#     def open_restaurant(self):
#         print(f"Ресторан {self.restaurant_name.title()} открывается в 12:00!")


# my_restaurant = Restaurant('гавайи','гавайской кухне')                
# your_restaurant = Restaurant('тай-тай','тайской кухне')                

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# your_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()    

#9.4
# print("\n")
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nНаш ресторан называется {self.restaurant_name.title()}.")
        print(f"Ресторан специплизируется на {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name.title()} открывается в 12:00!")

    def read_number(self):
        print(f"Ресторан посетило: {self.number_served} человек.")

    def set_number_served(self, customer): #Задаем значение посетителей
        self.number_served = customer  

    def increment_number_served(self, customer): #Увеличивает значение на количствао посетителей за день 
        self.number_served += customer
        


# my_rest = Restaurant('ош-халяль', 'узбекской кухни')
# my_rest.set_number_served(22)
# my_rest.increment_number_served(5)
# my_rest.read_number()





