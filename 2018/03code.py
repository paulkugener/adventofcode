#!/usr/bin/python3
from collections import defaultdict
import re

with open("03input.in", "r") as f:
    data = [line.strip() for line in f.readlines()]
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

m = defaultdict(list)
overlaps = {}

for (claim_number, start_x, start_y, width, height) in claims:
    overlaps[claim_number] = set()
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + height):
            if m[(i, j)]:
                for number in m[(i, j)]:
                    overlaps[number].add(claim_number)
                    overlaps[claim_number].add(number)
            m[(i, j)].append(claim_number)

print(len([k for k in m if len(m[k]) > 1]))
print([k for k in overlaps if len(overlaps[k]) == 0][0])
