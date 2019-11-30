#!/usr/bin/python3
from collections import defaultdict

# Edges
E = defaultdict(list)
# In-degree
D = defaultdict(int)

with open("07input.in", "r") as f:
    for line in f:
        data = [line.strip().split() for line in f.readlines()]
        E[data[1]].append(data[7])
        D[data[7]] += 1

for k in E:
    E[k] = sorted(E[k])


