

print("Введите 'quit' для выхода.\n")

while True:
    first_number = input("Введите первое число: ")
    if first_number == 'quit':
        break
    
    second_number = input("Введите второе число: ")
    if second_number == 'quit':
        break

    try: 
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Введите пожалуйста число!")
    else:
        print(answer)    
