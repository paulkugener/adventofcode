#!/usr/bin/env python3
import sys

bording_passes = []

with open("./2020/05input") as f:
    for line in f:
        bording_passes.append(line.strip())
     
def _seat_id(row, col):
    return row * 8 + col

def _decode_row(code):
    lo, hi = 0, 127
    for c in code:
        if c == 'F':
            hi = lo + (hi-lo)//2
        elif c == 'B':
            lo = hi - (hi-lo)//2
        else:
            print("ERROR 1")
            sys.exit()
    if lo != hi:
        print("ERROR 2")
        sys.exit()
    return lo

def _decode_col(code):
    lo, hi = 0, 7
    for c in code:
        if c == 'L':
            hi = lo + (hi-lo)//2
        elif c == 'R':
            lo = hi - (hi-lo)//2
        else:
            print("ERROR 1")
            sys.exit()
    if lo != hi:
        print("ERROR 2")
        sys.exit()
    return lo

def decode(code):
    row_code, col_code = code[:7], code[7:]
    row = _decode_row(row_code)
    col = _decode_col(col_code)
    return _decode_row(row_code), _decode_col(col_code)
        
def part1(bording_passes):
    # As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
    result = 0
    for p in bording_passes:
        row, col = decode(p)
        seat_id = _seat_id(row, col)
        if seat_id > result:
            result = seat_id
    return result

def part2(bording_passes):
    # What is the ID of your seat? Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
    l = []
    for r in range(12,104): 
        for c in range(8):
            l.append((r, c))
    #print(len(l))
    for p in bording_passes:
        row, col = decode(p)
        element_to_remove = (row, col)
        if element_to_remove in l:
            l.remove(element_to_remove)
    #print(len(l))
    #print(l)
    # (89, 2)
    return _seat_id(l[0][0], l[0][1])

print(part1(bording_passes))
print(part2(bording_passes))
