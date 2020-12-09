#!/usr/bin/env python3
import itertools, sys


#series = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576] #test

series = list()
with open("./2020/09input") as f:
    for line in f:
        series.append(int(line.strip()))
     

def part1():
    PREAMBLE_LENGTH = 25
    lo = 0
    hi = PREAMBLE_LENGTH
    index = PREAMBLE_LENGTH # this should be fine because in range STOP is exclusive

    while True:
        # copute all sums
        a = list(itertools.permutations(series[lo:hi], 2))
        b = [n+m for n, m in a]
        
        if series[index] in b:
            lo += 1
            hi += 1
            index += 1
        else:
            return series[index]

    return -1

def part2():
    GOAL = 144381670
    #GOAL = 127 # test
    
    # find a contiguous set of at least two numbers
    size = 2
    index = 0
    while True:
        if index+size == len(series):
            index = 0
            size += 1
            continue
        if sum(series[index:index+size]) == GOAL:
            break
        index += 1
    # add min and max from contiguous set
    r = series[index:index+size]
    return min(r) + max(r)


print(part1())
print(part2())
