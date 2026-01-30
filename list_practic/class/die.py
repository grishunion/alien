from random import randint
import random


digit_list = []
class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for digit in range(1, 11):
            digit = random.randint(1, self.sides)
            digit_list.append(digit)
                 
        
        
one_digit = Die()
one_digit.roll_die()
print(*digit_list)





            
       


        






        