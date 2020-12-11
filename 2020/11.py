#!/usr/bin/env python3
import copy
import sys


layout = list()
with open("./2020/11input") as f:
    for line_index, line in enumerate(f):
        layout.append([c for c in line.strip()])

# 3 states for each seat:
# - floor (.)
# - empty seat (L)
# - occupied seat (#)

# 3 rules are applied each round (tick) of the simulation:
# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.

def occupied_neighbors(state, row, col):
    # returns the number of neighboring occupied seats
    count = 0
    possible = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), 
        (row, col + 1),                     (row + 1, col + 1), 
        (row + 1, col), (row + 1, col - 1), (row, col - 1)
        ]
    for y, x in possible:
        if 0 <= y < len(state):
            if 0 <= x < len(state[y]):
                if state[y][x] == '#':
                    count += 1
    return count

def part1():
    # Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
    state = copy.deepcopy(layout)
    old_state = copy.deepcopy(layout)
    r = 1
    while True:
        state = copy.deepcopy(old_state)
        #print("round", r); r += 1
        for row_index in range(len(old_state)):
            for col_index in range(len(old_state[row_index])):
                if old_state[row_index][col_index] == '.': # Floor (.) never changes
                    continue
                occ = occupied_neighbors(old_state, row_index, col_index)
                if old_state[row_index][col_index] == 'L' and occ == 0: # empty
                    state[row_index][col_index] = '#'
                elif old_state[row_index][col_index] == '#' and occ >= 4: # occupied
                    state[row_index][col_index] = 'L'
        if state == old_state:
            break
        old_state = copy.deepcopy(state)
    return sum(x.count('#') for x in state)


def occupied_visible_neighbors(state, row, col):
    # returns the number of occupied & visible neighboring seats
    count = 0
    
    # get visible seats
    possible = []
    # north
    i = 1
    while True:
        if not 0 <= row-i < len(state):
            break
        if state[row-i][col] != '.':
            possible.append((row-i, col))
            break
        i += 1

    # north-east
    i = 1
    while True:
        if not 0 <= row-i < len(state) or not 0 <= col+i < len(state[0]):
            break
        if state[row-i][col+i] != '.':
            possible.append((row-i, col+i))
            break
        i += 1

    # east
    i = 1
    while True:
        if not 0 <= col+i < len(state[0]):
            break
        if state[row][col+i] != '.':
            possible.append((row, col+i))
            break
        i += 1

    # south-east
    i = 1
    while True:
        if not 0 <= row+i < len(state) or not 0 <= col+i < len(state[0]):
            break
        if state[row+i][col+i] != '.':
            possible.append((row+i, col+i))
            break
        i += 1
    
    # south
    i = 1
    while True:
        if not 0 <= row+i < len(state):
            break
        if state[row+i][col] != '.':
            possible.append((row+i, col))
            break
        i += 1

    # south-west
    i = 1
    while True:
        if not 0 <= row+i < len(state) or not 0 <= col-i < len(state[0]):
            break
        if state[row+i][col-i] != '.':
            possible.append((row+i, col-i))
            break
        i += 1

    # west
    i = 1
    while True:
        if not 0 <= col-i < len(state[0]):
            break
        if state[row][col-i] != '.':
            possible.append((row, col-i))
            break
        i += 1

    # south-west
    i = 1
    while True:
        if not 0 <= row-i < len(state) or not 0 <= col-i < len(state[0]):
            break
        if state[row-i][col-i] != '.':
            possible.append((row-i, col-i))
            break
        i += 1

    for y, x in possible:
        if state[y][x] == '#':
            count += 1
    return count

def part2():
    state = copy.deepcopy(layout)
    old_state = copy.deepcopy(layout)
    r = 1
    while True:
        state = copy.deepcopy(old_state)
        #print("round", r); r += 1
        for row_index in range(len(old_state)):
            for col_index in range(len(old_state[row_index])):
                if old_state[row_index][col_index] == '.': # Floor (.) never changes
                    continue
                occ = occupied_visible_neighbors(old_state, row_index, col_index)
                if old_state[row_index][col_index] == 'L' and occ == 0: # empty
                    state[row_index][col_index] = '#'
                elif old_state[row_index][col_index] == '#' and occ >= 5: # occupied
                    state[row_index][col_index] = 'L'
        if state == old_state:
            break
        old_state = copy.deepcopy(state)
    return sum(x.count('#') for x in state)


print(part1())
print(part2())
