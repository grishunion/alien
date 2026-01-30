# for value in range(1,21):
#     print(value)

digits = list(range(1,1_000_001))
print(min(digits))
print(max(digits))
print(sum(digits))

for value in range(1, 21, 2):
    print(value)

therds = []
for value in range(3, 31):
    if value % 3 == 0:
        therds.append(value)
print(therds)  

cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(cubes)    

generate_cubes = [value ** 3 for value in range(1,11)]
print(generate_cubes)