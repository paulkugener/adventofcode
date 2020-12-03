#!/usr/bin/env python3

grid = []
with open("./2020/03input") as f:
    for line in f:
        row = line.strip()
        grid.append(row)

def part1(grid, right, down):
    result = 0
    x = 0
    COLS = len(grid[0])
    for row in grid[::down]:
        if row[x%COLS] == '#':
            result += 1
        x += right
    return result

def part2(grid):
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] # (right, down)
    product = 1
    for r, d in moves:
        #print(part1(grid, r, d))
        product *= part1(grid, r, d)
    return product

print(part1(grid, 3, 1))
print(part2(grid))
