#!/usr/bin/env python3
import sys

rules = dict()

with open("./2020/07input") as f:
    for line in f:
        a, b = line.strip().split(' bags contain ')
        b = b.split(', ')
        tmp = list()
        for c in b:
            cc = c.split(' bag')[0]
            num = cc[0]
            if num == 'n':
                continue
            bag = cc[2:]
            tmp.append((num, bag))
        rules[a] = tmp

     
def part1():
    # How many bag colors can eventually contain at least one shiny gold bag?
    valid_bags = ['shiny gold']
    searching = True
    while searching:
        searching = False
        for k, v in rules.items():
            for c_num, c_bag in v:
                if c_bag in valid_bags and k not in valid_bags:
                    valid_bags.append(k)
                    searching = True
    return len(valid_bags) - 1

def unpack(bag):
    result = 0
    for i, j in rules[bag]:
        result += int(i) * unpack(j)
    return 1 + result

def part2():
    # How many individual bags are required inside your single shiny gold bag?
    # -> recursive
    return unpack('shiny gold') - 1


print(part1())
print(part2())
