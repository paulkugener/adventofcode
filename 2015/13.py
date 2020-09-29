#! python3

from collections import defaultdict
from itertools import permutations

happy_matrix = defaultdict(dict)
guests = set()

#with open("./2015/13test", "r") as f:
with open("./2015/13input", "r") as f:
    for line in f:
        guest, _, change, value, _, _, _, _, _, _, neighbor = line.rstrip().split(" ")
        if change == 'lose':
            value = 0 - int(value)
        elif change == "gain":
            value = 0 + int(value)
        neighbor = neighbor[:-1]

        happy_matrix.setdefault(guest, dict())[neighbor] = int(value)
        #happy_matrix.setdefault(neighbor, dict())[guest] = int(value) # the data are not symmetric

        guests.add(guest)
        guests.add(neighbor)

maxhappiness = 0
for ordering in permutations(guests):
    happiness = sum(happy_matrix[a][b]+happy_matrix[b][a] for a, b in zip(ordering, ordering[1:]))
    happiness += happy_matrix[ordering[0]][ordering[-1]] + happy_matrix[ordering[-1]][ordering[0]]
    maxhappiness = max(maxhappiness, happiness)

print(maxhappiness)


# 2

for i in list(happy_matrix.keys()):
    happy_matrix['me'][i] = 0
    happy_matrix[i]['me'] = 0

guests.add("me")

maxhappiness = 0
for ordering in permutations(guests):
    happiness = sum(happy_matrix[a][b]+happy_matrix[b][a] for a, b in zip(ordering, ordering[1:]))
    happiness += happy_matrix[ordering[0]][ordering[-1]] + happy_matrix[ordering[-1]][ordering[0]]
    maxhappiness = max(maxhappiness, happiness)

print(maxhappiness)
