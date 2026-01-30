# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

alien_0 = {'x_position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position : {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")  

print("\n")
favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pithon'
}

for name in favorite_languages.keys(): # аналогично с values()
    print(name.title())

print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\n")
for name in sorted(favorite_languages.keys()): #сортировка ключей
    print(f"{name.title()}, thank you for taking the poll.")        


print("\n")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")