#!/usr/bin/env python3
from collections import defaultdict

groups = defaultdict(list)

with open("12input.txt", "r") as f:
    for line in f:
        line_list = line.split()
        a = int(line_list[0])
        bs = [int(x.strip(',')) for x in line_list[2:]]
        for b in bs:
            groups[a].append(b)
            groups[b].append(a)

q = [0]
visited = set()
while q:
    a = q.pop()
    for b in groups[a]:
        if b not in visited:
            visited.add(b)
            q.append(b)

print(len(visited)) # part 1

visited = set()
num_of_groups = 0
for i in range(max(groups)):
    if i in visited:
        continue
    num_of_groups += 1
    q = [i]
    while q:
        a = q.pop()
        for b in groups[a]:
            if b not in visited:
                visited.add(b)
                q.append(b)

print(num_of_groups) # part 2
