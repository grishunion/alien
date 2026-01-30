
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())    


age = 19
if age >= 18:
    print("\nYou are old enough to vote!")        
    print("Have you registred to vote yet!")

print("\n")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 40    
else: 
    price = 20

print(f"Your admission cost is ${price}.")  

print("\n")
requested_toppinngs = ['mushroms', 'extra cheese']
if 'mushroms' in requested_toppinngs:
    print("Adding mushroms.")
if 'pepperoni' in requested_toppinngs:
    print("Adding pepperoni.")    
if 'extra cheese' in requested_toppinngs:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("\n")
requested_toppings = ['mushroms', 'extra cheese', 'green peppers']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:    
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")    

print("\n")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are your sure you want a plain pizza?")   

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'frech fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")            

  
