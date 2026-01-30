# prompt = "\nВведите пожалуйста название ингридиентов к пицце."
# prompt += "\nДля выхода из набора введите 'quit': "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         # active = False
#         break
#     else:
#         print(f"{message.title()}-добавлен в пиццу!")


# 7.5

# prompt = "Введите пожалуйста ваш возраст: "

# active = True
# while active:
#     age = input(prompt)
#     age = int(age)
    
#     if age <= 3:
#         print(f"Для вас вход бесплатный!")
#     if 3 < age <= 12:
#         print(f"Стоимость билета для вас 10$.") 
#     if age > 12:
#         print(f"Стоимость билета для вас 15$.")       
    

sandwich_orders = ['gamburger','pastrami', 'cheeseburger', 'pastrami', 'fishburger', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Pastrami more not")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nYour sandwich:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()}")