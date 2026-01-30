# prompt = "Какую машину вы хотели бы взять в каршеринг? "
# car = input(prompt)
# print(f"Я хотел бы, {car.title()}!")

# prompt = "Здравствуйте сэр, сколько мест вы хотите забронировать? "
# site = input(prompt)
# site = int(site)

# if site > 8:
#     print("К сожалению придется подождать сэр!")
# else:
#     print("Ваш стол готов, просим вас!")

digit = input("Введите число: ")
digit = int(digit)
if digit % 10 == 0:
    print("Ваше число кратно 10!")
else:
    print("Ваше число некратно 10!")    