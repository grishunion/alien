user_0 = {
    'first_name' : 'alex',
    'last_name' : 'gri',
    'age' : '37',
    'city' : 'ulyanovsk'
}
user_1 = {
    'first_name' : 'alexei',
    'last_name' : 'grish',
    'age' : '35',
    'city' : 'ulyanovsk'
}
user_2 = {
    'first_name' : 'anna',
    'last_name' : 'grishunina',
    'age' : '39',
    'city' : 'kemerovo'
}

users = [user_0, user_1, user_2]
for user in users:
    print(user)



for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value.title()}")

print("\n")

rivers = {
    'nile' : 'egypt',
    'volga': 'russia',
    'dnepr': 'ukraine'
}    

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")


favorite_places = {
    'alex': {
        'monument': 'red square',
        'country': 'russia',
        'city': 'moscow',
        'year': 1493,
    },
    'anna': {
        'monument': 'motherland',
        'country': 'russia',
        'city': 'volgograd',
        'year': 1967,

    },
    'fedor': {
        'monument': 'eiffel tower',
        'country': 'france',
        'city': 'paris',
        'year': 1889, 
    },

}
for user_name, user_info in favorite_places.items():
    print(f"\n{user_name.title()} likes {user_info['monument'].title()}.")
    full_location = f"{user_info['country']}, {user_info['city']}"
    print(f"The monument was built in the {user_info['year']} and is located {full_location.title()}.")








