#!/usr/bin/env python3

jList = list()

with open("5input.txt", "r") as f:
    for line in f:
        jList.append(int(line))

def part1():
    lList = list(jList)
    i = 0
    steps = 0
    while(i in range(len(lList))):
        jVal = lList[i]
        lList[i] += 1
        i += jVal
        steps += 1
    return steps


def part2():
    lList = list(jList)
    i = 0
    steps = 0
    while(i in range(len(lList))):
        jVal = lList[i]
        if jVal >= 3:
            lList[i] -= 1
        else:
            lList[i] += 1
        i += jVal
        steps += 1
    return steps


print(part1()) # 339351
print(part2()) # 24315397
