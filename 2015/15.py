#! python3

from collections import defaultdict
from pprint import pprint

# init

ingredients = defaultdict(dict)

#with open("./2015/15test", "r") as f:
with open("./2015/15input", "r") as f:
    for line in f:
        ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.rstrip().split(" ")

        ingredient = ingredient[:-1]
        capacity = int(capacity[:-1])
        durability = int(durability[:-1])
        flavor = int(flavor[:-1])
        texture = int(texture[:-1])
        calories = int(calories)

        ingredients[ingredient] = {
            'capacity': capacity, 
            'durability': durability, 
            'flavor': flavor, 
            'texture': texture,
            'calories': calories
        }

pprint(ingredients)

# compute

result1 = 0
result2 = 0

number_of_tbls = 100
for i in range(number_of_tbls+1):
    for j in range(number_of_tbls-i+1):
        for k in range(number_of_tbls-i-j+1):
            l = number_of_tbls-i-j-k
            properties = [i*ingredients['Frosting'][p] + j*ingredients['PeanutButter'][p] + k*ingredients['Sprinkles'][p] + l*ingredients['Sugar'][p] for p in ['capacity', 'durability', 'flavor', 'texture', 'calories']]
            if min(properties[:4]) <= 0:
                continue
            objective_value = 1
            for x in properties[:4]:
                objective_value *= x
            #print(i, j, properties, objective_value)
            if objective_value > result1:
                result1 = objective_value
            if properties[4] == 500 and objective_value > result2:
                result2 = objective_value

print(result1)
print(result2)
