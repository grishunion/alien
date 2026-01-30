
from random import randint
import random

list_comb = [3, 7]
combination_win = [3, 7]
combination = []
class Win():
    def __init__(self, sides=3):
        self.sides = sides

    def combinat(self):
        for comb in range(1, self.sides):
            comb = random.choice(list_comb)
            combination.append(comb)

    def winner(self):
        while True:
            if combination == combination_win:
                print("You win!")
                break   
            else:
                print("You lose")    
            

     

lottery = Win()
lottery.combinat()
print(combination)
print(combination_win)
lottery.winner()

        