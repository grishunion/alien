
players = ['chales', 'matina', 'michail','florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canolli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)




