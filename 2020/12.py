#!/usr/bin/env python3
import sys


instructions = list()
with open("./2020/12input") as f:
    for line in f:
        a, v = line.strip()[0], int(line.strip()[1:])
        instructions.append((a, v))


def part1():
    # What is the Manhattan distance between that location and the ship's starting position?
    o = 1
    x, y = 0, 0
    for a, v in instructions:
        #print(x, y)
        if a == 'N':
            y += v
        elif a == 'E':
            x += v
        elif a == 'S':
            y -= v
        elif a == 'W':
            x -= v
        elif a == 'L':
            #print("---", a, v, o)
            o = ((o - v/90) + 4) % 4
            #print(o)
        elif a == 'R':
            #print("---", a, v, o)
            o = ((o + v/90) + 4) % 4
            #print(o)
        elif a == 'F':
            if o == 0:
                y += v
            elif o == 1:
                x += v
            elif o == 2:
                y -= v
            elif o == 3:
                x -= v
        else:
            print("ERR", a, o)
            sys.exit()
    return abs(x) + abs(y)


def part2():
    # What is the Manhattan distance between that location and the ship's starting position?
    ship_x, ship_y = 0, 0
    x, y = 10, 1 # waypoint
    for a, v in instructions:
        if a == 'N':
            y += v
        elif a == 'E':
            x += v
        elif a == 'S':
            y -= v
        elif a == 'W':
            x -= v
        elif a == 'L':
            if v == 270:
                x, y = y, -x
            elif v == 180:
                x, y = -x, -y
            elif v == 90:
                x, y = -y, x
            else:
                print("ERR", a, v)
                sys.exit()
        elif a == 'R':
            if v == 90:
                x, y = y, -x
            elif v == 180:
                x, y = -x, -y
            elif v == 270:
                x, y = -y, x
            else:
                print("ERR", a, v)
                sys.exit()
        elif a == 'F':
            for _ in range(v):
                ship_x += x
                ship_y += y
        else:
            print("ERR", a, v)
            sys.exit()
    return abs(ship_x) + abs(ship_y)


print(part1())
print(part2())
