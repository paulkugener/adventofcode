#!/usr/bin/env python3
from collections import Counter
import sys


adapters = list()
with open("./2020/10input") as f:
    for line in f:
        adapters.append(int(line.strip()))

# adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4] #test1
# adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3] #test2
     

def part1():
    # What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
    CHARGING_OUTLET = 0
    diff = [0,0,0,0]
    adapters.sort()
    j = CHARGING_OUTLET
    for i in adapters:
        diff[i-j] += 1
        j = i
    # don't miss the last +3
    diff[3] += 1
    return diff, diff[1]*diff[3]


def part2():
    # What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
    # /u/ephemient 
    nums = sorted(map(int, adapters))
    counter = Counter((0, ))
    for num in nums:
        counter[num] += sum(counter[i] for i in range(num - 3, num))
    return counter[nums[-1]]


print(part1())
print(part2())
