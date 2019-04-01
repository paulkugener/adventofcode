#!/usr/bin/env python3
import itertools

result1 = 0
result2 = 0

with open("2input.txt", "r") as f:
    for line in f:
        linelist = line.split()
        linelist = list(map(int, linelist))
        result1 += max(linelist) - min(linelist)

        for i in itertools.combinations(linelist, 2): # make tupels of two for members of linelist and iterate
            if max(i) % min(i) == 0: # if evenly divides...
                result2 += int(max(i) / min(i))
                # dont need break because there are no "repeat tupels"

print("answer1 = " + str(result1)) # solution1 = 42378
print("answer2 = " + str(result2)) # solution2 = 246
