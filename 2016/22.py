#!/usr/bin/env python3
from collections import defaultdict

# inspired by /u/jlweinkam
# I really like the idea of not using a list of lists to travel around the 'map'
# because "growing" the map would be tedious!
# Instead we just use a defaultdict where the keys are the positions!

with open('22input.txt') as f:
    lines = f.read().splitlines()

# part 1
grid = defaultdict(chr)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[(i,j)] = lines[i][j]

y = int(len(lines) / 2)
x = int(len(lines[0]) / 2)
d = 'U' # U, R, D, L
infections = 0

for _ in range(10_000):
    if (y,x) not in grid.keys():
        grid[y,x] = '.'
    if grid[y,x] == '#': # turn right and clean
        if d == 'U':
            d = 'R'
        elif d == 'R':
            d = 'D'
        elif d == 'D':
            d = 'L'
        elif d == 'L':
            d = 'U'
        grid[y,x] = '.'
    elif grid[y,x] == '.': # turn left and infect
        if d == 'U':
            d = 'L'
        elif d == 'R':
            d = 'U'
        elif d == 'D':
            d = 'R'
        elif d == 'L':
            d = 'D'
        grid[y,x] = '#'
        infections += 1
    if d == 'U': # move!
        y -= 1
    elif d == 'R':
        x += 1
    elif d == 'D':
        y += 1
    elif d == 'L':
        x -= 1

print("part 1:", infections)

# part 2
grid = defaultdict(chr)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[(i,j)] = lines[i][j]

y = int(len(lines) / 2)
x = int(len(lines[0]) / 2)
d = 'U' # U, R, D, L
infections = 0

for _ in range(10_000_000):
    if (y,x) not in grid.keys():
        grid[y,x] = '.'
    if grid[y,x] == '.': # turn left and weaken
        if d == 'U':
            d = 'L'
        elif d == 'R':
            d = 'U'
        elif d == 'D':
            d = 'R'
        elif d == 'L':
            d = 'D'
        grid[y,x] = 'W'
    elif grid[y,x] == 'W': # infect
        grid[y,x] = '#'
        infections += 1
    elif grid[y,x] == '#': # turn right and flag
        if d == 'U':
            d = 'R'
        elif d == 'R':
            d = 'D'
        elif d == 'D':
            d = 'L'
        elif d == 'L':
            d = 'U'
        grid[y,x] = 'F'
    elif grid[y,x] == 'F': # reverse direction and clean
        if d == 'U':
            d = 'D'
        elif d == 'R':
            d = 'L'
        elif d == 'D':
            d = 'U'
        elif d == 'L':
            d = 'R'
        grid[y,x] = '.'
    if d == 'U': # move!
        y -= 1
    elif d == 'R':
        x += 1
    elif d == 'D':
        y += 1
    elif d == 'L':
        x -= 1

print("part 2:", infections)
