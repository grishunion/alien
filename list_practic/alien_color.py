alien_color = 'yellow'
if alien_color == 'green':
    point = 5
elif alien_color =='yellow':
    point = 10
else:
    point = 15        
print(f"Your won {point} points now!")    

print("\n")

age = 33
if age < 2:
    print("Младенец")
elif 2 <= age < 4:
    print("Малыш")
elif 4 <= age < 13:
    print("Ребенок")   
elif 13 <= age < 20:
    print("Подросток")
elif 20 <= age < 65:
    print("Взрослый") 
elif age >= 65:
    print("Пожилой человек")  

print("\n")
favorite_fruits = ['apple', 'pineapple']
if 'banana' in favorite_fruits:
    print("You really like bananas!")                  
if 'apple' in favorite_fruits:
    print("You really like apples!")    
if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")      