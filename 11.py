#!/usr/bin/env python3

fstr = open("11input.txt", "r").readline()
steps = fstr.split(",")

# about hex grids: https://www.redblobgames.com/grids/hexagons/
#   +y n  -z
#  nw +--+ ne
#    /    \
# -x+      ++x
#    \    /
#  sw +--+ se
#   +z s -y

x, y, z = 0, 0, 0
max_dist = 0


# Manhattan distance to origin
def cube_distance():
    return (abs(0 - x) + abs(0 - y) + abs(0 - z)) / 2


i = 0
while True:
    if i >= len(steps):
        break
    if steps[i] == 'n':
        y += 1
        z -= 1
    if steps[i] == 'ne':
        x += 1
        z -= 1
    if steps[i] == 'se':
        y -= 1
        x += 1
    if steps[i] == 's':
        y -= 1
        z += 1
    if steps[i] == 'sw':
        x -= 1
        z += 1
    if steps[i] == 'nw':
        x -= 1
        y += 1
    if cube_distance() > max_dist:
        max_dist = cube_distance()
    i += 1


print("finish coords = ({}, {}, {})".format(x, y, z))
print("manhatten dist = {}".format(int(cube_distance()))) # part 1
print("max distance from home = {}".format(int(max_dist))) # part 2
