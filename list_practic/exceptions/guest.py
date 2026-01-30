#10.3
# filename = 'list_practic/exceptions/guest.txt'
# guest_name = input("Введите ваше имя: ")
# with open(filename, 'w') as file_object:
#     file_object.write(guest_name.title())

filename = 'list_practic/exceptions/guest.txt'


while True:
    guest_name = input("Введите ваше имя: ")

    if guest_name == 'q':
          break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest_name.title()}\n")
            print(f"Добро пожаловать {guest_name.title()}")
                

        

    

