
# def greet_user(username):
#     """Выводит простое приветствие."""
#     print(f"Hello, {username.title()}!")
# greet_user('jessi')    
# greet_user('sarah') 

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry') #именнованый аргумент
# describe_pet('dog', 'willie')    


# def describe_pet(pet_name, animal_type='dog'):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry') #именнованый аргумент
# describe_pet('willie')   

# print('\n')
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musican = get_formatted_name('jimi', 'hendrix')
# print(musican)
# musican = get_formatted_name('john', 'hooker', 'lee')
# print(musican)

# print("\n")
# def build_person(first_name, last_name, age=None):
#     """Возвращает информацию о человеке"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musican = build_person('jimi', 'hendrix', age=27)
# print(musican)

# print("\n")
# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\n--- Hello, {formatted_name}! ---")  

print("\n")

def greet_users(names):
    """Вывод простого приветствия для каждого пользователя в списке."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)        

print("\n")

def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza(16, 'pepperoni')    
make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')   


def build_profile(first, last, **user_info):
    """Строит с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='phisics')
print(user_profile)

