#! python3
# from /u/semi225599 in https://www.reddit.com/r/adventofcode/comments/3y1s7f/day_24_solutions/
from functools import reduce
from itertools import combinations
from operator import mul

weights = []

with open("./2015/24input", "r") as f:
    for line in f:
        i = int(line.rstrip())
        weights.append(i)

def day24(num_groups):
    group_size = sum(weights) // num_groups
    for i in range(len(weights)):
        quantum_entanglements = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == group_size]
        if quantum_entanglements:
            return min(quantum_entanglements)

print(day24(3))
print(day24(4))
