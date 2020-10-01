#! python3

from itertools import combinations

eggnogg = 150
c = []
result1 = 0
result2 = 0

with open("./2015/17input", "r") as f:
    for line in f:
        line = line.rstrip()
        c.append(int(line))

for i in range(len(c)-1):
    for perm in combinations(c, i):
        if sum(perm) == eggnogg:
            result1 += 1
    if result1 and not result2:
        result2 = result1

print(result1)
print(result2)
