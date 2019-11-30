#!/usr/bin/python3
import itertools

with open("01input.in", "r") as f:
    data = [int(x) for x in f.readlines()]

# Part 1
print(sum(data))

# Part 2
freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)
