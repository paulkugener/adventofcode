#!/usr/bin/env python3
import math
from itertools import count
import sys

earliest = 0
buses = list()
buses2 = list()
with open("./2020/13input") as f:
    lines = f.readlines()
    earliest = int(lines[0].strip())
    buses = [int(i) for i in lines[1].strip().split(',') if i.isnumeric()]
    buses2 = [(i, int(bus_id)) for i, bus_id in enumerate(lines[1].split(',')) if bus_id != 'x']


def part1():
    # What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
    d = dict()
    for bus_id in buses:
        d[bus_id] = math.ceil(earliest / bus_id) * bus_id
    best_bus_id = min(d.keys(), key=(lambda k: d[k]))
    return best_bus_id * (d[best_bus_id] - earliest)


def part2():
    # What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
    jump = buses2[0][1]
    time_stamp = 0
    for delta, bus_id in buses2[1:]:
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp


print(part1())
print(part2())
