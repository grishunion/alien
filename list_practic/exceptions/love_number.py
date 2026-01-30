
import json

number = input("Введите число: ")
filename = 'number.json'

with open(filename, 'w') as f:
    json.dump(number, f)
    print("Мы запомнили ваше число")
   