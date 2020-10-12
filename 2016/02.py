#!/usr/bin/env python3
import sys

PAD = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

cur = (1, 1)  # start at '5'

INSTR = {
    "U": (0, -1),
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0)
}

instructions = []
with open("./2016/02input") as f:
    for line in f:
        line_list = line.rstrip()
        instructions.append(line_list)

for n in instructions:
    for i in n:
        cur = (max(0, min(cur[0] + INSTR[i][0], 2)),
               max(0, min(cur[1] + INSTR[i][1], 2)))
    print(PAD[cur[1]][cur[0]], end="")

# part 2
print()

PAD2 = [['x', 'x', '1', 'x', 'x'],
        ['x', '2', '3', '4', 'x'],
        ['5', '6', '7', '8', '9'],
        ['x', 'A', 'B', 'C', 'x'],
        ['x', 'x', 'D', 'x', 'x']]

cur = (0, 2)  # start at '5'
prev = cur

for n in instructions:
    for i in n:
        cur = (max(0, min(cur[0] + INSTR[i][0], 4)),
               max(0, min(cur[1] + INSTR[i][1], 4)))
        if PAD2[cur[1]][cur[0]] == 'x':
            cur = prev
        prev = cur
    print(PAD2[cur[1]][cur[0]], end="")
    