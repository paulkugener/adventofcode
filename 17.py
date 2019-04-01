#!/usr/bin/env python3

def part1(step):
    buffer = [0]
    pos = 0
    cycle = 2017
    for j in range(1, cycle + 1):
        # define next pos
        pos = ((pos + step) % len(buffer)) + 1
        # insert value at pos
        buffer.insert(pos, j)
    return buffer[buffer.index(cycle) + 1]

from collections import deque
def part2(step):
    buffer = deque([0])
    cycle = 50_000_000
    for j in range(1, cycle + 1):
        buffer.rotate(-step)
        buffer.append(j)
    return buffer[buffer.index(0) + 1]

puzzle_input = 303
print(part1(puzzle_input))
print(part2(puzzle_input))
