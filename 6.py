#!/usr/bin/env python3

p_input = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
p_input = p_input.split()
p_input = list(map(int, p_input))
p_input = [0, 2, 7, 0]

seen = list()

while p_input not in seen:
    seen.append(list(p_input))
    m = max(p_input)
    i = p_input.index(m)
    p_input[i] = 0
    while m > 0:
        i += 1
        if i == len(p_input):
            i = 0
        p_input[i] += 1
        m -= 1

print(len(seen))
print(len(seen) - seen.index(p_input)) # ty /u/vash3r
