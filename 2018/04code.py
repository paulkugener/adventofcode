#!/usr/bin/python3
from collections import defaultdict

lines = open('04input.in').read().split('\n')
lines.sort()

def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])

C = defaultdict(int)
CM = defaultdict(int)
guard = None
asleep = None

for line in lines:
    if line:
        time = parseTime(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for t in range(asleep, time):
                CM[(guard, t)] += 1
                C[guard] += 1

def part2():
    best = None
    for k, v in CM.items():
        if best is None or v > CM[best]:
            best = k
    return best

def part1():
    best_guard = max(C, key=lambda key: C[key])
    best = None
    for k, v in CM.items():
        if best_guard in k:
            if best is None or v > CM[best]:
                best = k
    return best

best_guard, best_min = part1()  
print(best_guard, best_min)
print(best_guard * best_min)

best_guard, best_min = part2()
print(best_guard, best_min)
print(best_guard * best_min)
