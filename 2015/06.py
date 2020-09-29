#! python3

import numpy as np 

grid_1 = np.zeros((1_000, 1_000), dtype='bool')
grid_2 = np.zeros((1_000, 1_000), dtype='int')

def str_to_coords(instr):
    return [int(x) for x in instr.split(",")]

def turn_lights_on(start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            grid_1[x, y] = True
            grid_2[x, y] += 1

def turn_ligths_off(start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            grid_1[x, y] = False
            grid_2[x, y] = max(0, grid_2[x, y]-1)

def toggle_lights(start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            grid_1[x, y] = not grid_1[x, y]
            grid_2[x, y] += 2

with open("./2015/06input") as f:
    for line in f:
        instruction = line.rstrip("\n\r").split(" ")
        if instruction[0] == "turn":
            start_x, start_y = str_to_coords(instruction[2])
            end_x, end_y = str_to_coords(instruction[4])
            if instruction[1] == "on":
                turn_lights_on(start_x, start_y, end_x, end_y)
            else:
                turn_ligths_off(start_x, start_y, end_x, end_y)
        else:
            start_x, start_y = str_to_coords(instruction[1])
            end_x, end_y = str_to_coords(instruction[3])
            toggle_lights(start_x, start_y, end_x, end_y)

count = 0 # 1
brightness = 0 # 2

for x in range(0, len(grid_1)):
    for y in range(0, len(grid_1[0])):
        if grid_1[x, y]:
            count += 1
        brightness += grid_2[x, y]

print(count)
print(brightness)
