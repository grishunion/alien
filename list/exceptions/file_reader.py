

# file_path = 'list/exceptions/pi_digits.txt' #Абсолютный путь
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)

filename = 'list/exceptions/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))