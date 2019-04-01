#!/usr/bin/env python3
import numpy as np

def translate_to_np(s):
    return np.array([[c == '#' for c in l] for l in s.split('/')])

def enhance(grid):
    size = len(grid)
    by = 2 if size % 2 == 0 else 3
    new_size = size * (by+1) // by
    solution = np.empty((new_size, new_size), dtype=bool)
    squares = range(0, size, by)
    new_squares = range(0, new_size, by+1)

    for i, ni in zip(squares, new_squares):
        for j, nj in zip(squares, new_squares):
            square = grid[i:i+by, j:j+by]
            enhanced = mappings[square.tobytes()]
            solution[ni:ni+by+1, nj:nj+by+1] = enhanced
    return solution

def solve(part):
    grid = translate_to_np(start)
    iterations = 5 if part == 1 else 18
    for _ in range(iterations):
        grid = enhance(grid)
    return int(grid.sum())


with open('21input.txt') as f:
    rules = f.readlines()

    mappings = {}
    start = '.#./..#/###'

    for line in rules:
        k, v = map(translate_to_np, line.strip().split(' => '))
        for a in (k, np.fliplr(k)):
            for r in range(4):
                mappings[np.rot90(a, r).tobytes()] = v

    print("part 1 =", solve(part=1))
    print("part 2 =", solve(part=2))
