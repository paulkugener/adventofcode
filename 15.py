#!/usr/bin/env python3

# Generator A starts with 289
# Generator B starts with 629
lastA = 289
lastB = 629

def part1(a, b):
    lastA, lastB = a, b
    result = 0
    opservations = 40000000
    i = 0
    while i < opservations:
        currA = (lastA * 16807) % 2147483647
        currB = (lastB * 48271) % 2147483647
        # convert to binary
        binA = format(currA, '032b')
        binB = format(currB, '032b')
        # compare last 16 bits
        if binA[16:] == binB[16:]:
            result += 1
        lastA, lastB = currA, currB
        i += 1
    return result

def part2(a, b):
    lastA, lastB = a, b
    result = 0
    opservations = 5000000
    i = 0
    while i < opservations:
        currA = (lastA * 16807) % 2147483647
        while currA % 4 != 0:
            currA = (currA * 16807) % 2147483647
        currB = (lastB * 48271) % 2147483647
        while currB % 8 != 0:
            currB = (currB * 48271) % 2147483647
        # convert to binary
        binA = format(currA, '032b')
        binB = format(currB, '032b')
        # compare last 16 bits
        if binA[16:] == binB[16:]:
            result += 1
        lastA, lastB = currA, currB
        i += 1
    return result

#print(part1(lastA, lastB))
print(part2(lastA, lastB))
