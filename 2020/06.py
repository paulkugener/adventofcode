#!/usr/bin/env python3
import sys

declarations = []

with open("./2020/06input") as f:
    g = list() # the one current group
    for line in f:
        if line == '\n':
            declarations.append(g)
            g = list()
            continue
        g.append(line.strip())
    declarations.append(g) # we need this for the last group from the input
     
def part1(declarations):
    # For each group, count the number of questions to which **anyone** answered "yes". What is the sum of those counts?
    result = 0
    for group in declarations:
        tmp_string = ""
        for person in group:
            tmp_string += person
        tmp_set = set(tmp_string)
        result += len(tmp_set)
    return result

def part2(declarations):
    # For each group, count the number of questions to which **everyone** answered "yes". What is the sum of those counts?
    # -> Intersection
    result = 0
    for group in declarations:
        tmp_set = set("abcdefghijklmnopqrstuvwxyz")
        for person_string in group:
            tmp_set = tmp_set.intersection(person_string)
        result += len(tmp_set)
    return result

print(part1(declarations))
print(part2(declarations))
