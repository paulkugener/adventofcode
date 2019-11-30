#!/usr/bin/python3
from collections import Counter
 
with open("06input.in", "r") as f:
    locations = [line.strip().split(', ') for line in f.readlines()]
    locations = [[int(i) for i in l] for l in locations]

# scope of locations
x_min = min(l[0] for l in locations)
x_max = max(l[0] for l in locations) + 1
y_min = min(l[1] for l in locations)
y_max = max(l[1] for l in locations) + 1

m = {}

for i in range(x_min, x_max):
    for j in range(y_min, y_max):
        d = min(abs(i-x) + abs(j-y) for x, y in locations)
        for n, (x, y) in enumerate(locations):
            if abs(i-x) + abs(j-y) == d:
                if m.get((i, j), -1) != -1:
                    m[i, j] = -1
                    break 
                m[i, j] = n

s = set([-1])
s = s.union(set(m[x, y_max-1] for x in range(x_min, x_max)))
s = s.union(set(m[x,   y_min] for x in range(x_min, x_max)))
s = s.union(set(m[x_max-1, y] for y in range(y_min, y_max)))
s = s.union(set(m[x_min,   y] for y in range(y_min, y_max)))

print(next(i[1] for i in Counter(m.values()).most_common() if i[0] not in s))

print(sum(sum(abs(i-x) + abs(j-y) for x, y in locations) < 10000 for i in range(x_min, x_max) for j in range(y_min, y_max)))
