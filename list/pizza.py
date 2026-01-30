#Сохранение информации о заказной пицце
# pizza = {
#     'crust': 'trick',
#     'toppings': ['mushrooms', 'extra cheese'],

# }

# #Описание заказа 
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)

# print("\n")
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'prinston',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }

# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")


def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
