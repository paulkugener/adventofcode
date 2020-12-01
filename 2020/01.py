#!/usr/bin/env python3
import sys

entries = []
with open("./2020/01input") as f:
    for line in f:
        entries.append(int(line.strip()))

def part1(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            if i == j:
                continue
            if entries[i] + entries[j] == 2020:
                return entries[i], entries[j], entries[i] * entries[j]

def part2(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                if i == j or i == k or j == k:
                    continue
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i], entries[j], entries[k], entries[i] * entries[j] * entries[k]
        
print(part1(entries))
print(part2(entries))
