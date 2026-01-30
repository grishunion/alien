list_pizza = ['pepperoni', 'double cheese', 'margarita']

for pizza in list_pizza:
    print(f"I like {pizza} pizza!")
print(f"I really like pizza!")

print("\n")
users = ['alex', 'nastya', 'gleb', 'toyo', 'admin']

if len(users) == 0:
    print("We need to ind some users!")
else:
    for user in users:
        if user == 'admin':
            print(f"\nHello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")  

print("\n")
current_users = ['alex', 'nastya', 'gleb', 'toyo', 'admin']  
current_users_low = current_users[:]

new_users = ['michail', 'lora', 'GLEB', 'toyo', 'foma']

for new_user in new_users:
    if new_user.lower() in current_users_low:
        print(f"Please {new_user.title()}, choose a new name!")
    else:
        print(f"Welcome {new_user.title()}.")    


print("\n")
digits = []
digits_new = []
for value in range(1,11):
    digits.append(value)
print(*digits, sep=', ')    

for digit in digits:
    if digit == 1:
        digit = str(digit) + 'st'
        digits_new.append(digit)
    elif digit == 2:
        digit = str(digit) + 'nd'
        digits_new.append(digit)
    elif digit == 3:
        digit = str(digit) + 'rd'
        digits_new.append(digit)
    else:
        digit = str(digit) + 'th'
        digits_new.append(digit)       

print(*digits_new, sep=', ')      


#6.7

