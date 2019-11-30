#!/usr/bin/env python3

components = list()
with open('24input.txt') as f:
    for line in f:
        components.append(list(map(int, line.strip().split('/'))))    

lengths = list()
def find_next(port, remaining, cur_total, length):
    lengths.append([length, cur_total])

    for next_port in remaining:
        x, y = next_port

        if x == port or y == port:
            new_remaining = [new_c for new_c in remaining if new_c != next_port]
            find_next(x if y == port else y, new_remaining, cur_total + sum(next_port), length + 1)

for c in components:
    x, y = c
    if x == 0 or y == 0:
        remaining = [new_c for new_c in components if new_c != c]
        # ~more readable but the same~
        # remaining = components.copy()
        # remaining.remove(c)
        find_next(x if y == 0 else y, remaining, sum(c), 1)

print(max([length[1] for length in lengths]))
longest = max([length[0] for length in lengths])
print(max([length[1] for length in lengths if length[0] == longest]))
