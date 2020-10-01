#! python3

from collections import defaultdict
from pprint import pprint

# init

sue_d = defaultdict(dict)
bad_chars = [':', ',']

with open("./2015/16input", "r") as f:
    for line in f:
        for b in bad_chars:
            line = line.replace(b, '')
        _, i, a, an, b, bn, c, cn = line.rstrip().split(" ")

        sue_d[int(i)] = {
            a: int(an), 
            b: int(bn), 
            c: int(cn)
        }

#pprint(sue_d)

# TARGET SUE
target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

# search part1
for s in sue_d:
    counter = 0
    for pk, pv in target.items():
        if pk in sue_d[s]:
            if pv == sue_d[s][pk]:
                counter += 1
    if counter >= 3:
        print(s)

# search part2
for s in sue_d:
    counter = 0
    for pk, pv in target.items():
        if pk == "cats" or pk == "trees":
            if pk in sue_d[s]:
                if pv < sue_d[s][pk]:
                    counter += 1
        elif pk == "pomeranians" or pk == "goldfish":
            if pk in sue_d[s]:
                if pv > sue_d[s][pk]:
                    counter += 1
        else:
            if pk in sue_d[s]:
                if pv == sue_d[s][pk]:
                    counter += 1
    if counter >= 3:
        print(s)
