#!/usr/bin/env python3
import sys

instructions = []
with open("./2016/01input") as f:
    for line in f:
        line_list = line.rstrip().split(",")
        for i in line_list:
            i = i.replace(" ", "")
            t = (i[0], int(i[1:]))
            instructions.append(t)

orientation = 0 # n=0, e=1, s=2, w=3

x = 0
y = 0

# part 1

# for i in instructions:
#     if i[0] == 'R':
#         orientation += 1
#         if orientation == 4:
#             orientation = 0
#     elif i[0] == 'L':
#         orientation -= 1
#         if orientation == -1:
#             orientation = 3
#     else:
#         sys.exit("ERROR: turn instruction")

#     if orientation == 0:
#         y -= i[1]
#     elif orientation == 1:
#         x += i[1]
#     elif orientation == 2:
#         y += i[1]
#     elif orientation == 3:
#         x -= i[1]
#     else:
#         sys.exit("ERROR: distance instruction")

# print("bunny HQ: location(", x, y, "), distance", abs(x)+abs(y))


# part 2
visited = [(x,y)]

for i in instructions:
    if i[0] == 'R':
        orientation += 1
        if orientation == 4:
            orientation = 0
    elif i[0] == 'L':
        orientation -= 1
        if orientation == -1:
            orientation = 3
    else:
        sys.exit("ERROR: turn instruction")

    distance = i[1]
    while(distance != 0):
        if orientation == 0:
            y -= 1
        elif orientation == 1:
            x += 1
        elif orientation == 2:
            y += 1
        elif orientation == 3:
            x -= 1
        else:
            sys.exit("ERROR: distance instruction")
        distance -= 1
        
        loc = (x,y)
        if loc in visited:
            print("bunny HQ 2: location", loc, ", distance", abs(x)+abs(y))
            sys.exit()
        else:
            visited.append(loc)
