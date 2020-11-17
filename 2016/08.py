#!/usr/bin/env python3
import numpy as np

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6

screen = np.zeros([SCREEN_HEIGHT, SCREEN_WIDTH], dtype=bool)

def print_screen():
    result = ''
    for i in screen:
        for j in i:
            if j == False:
                result += '.'
            elif j == True:
                result += '#'
        result += '\n'
    print(result)

def number_of_on_pixels():
    return np.count_nonzero(screen == True)

instructions = []

with open("./2016/08input") as f:
    for line in f:
        line = line.rstrip()
        instructions.append(line)

for i in instructions:
    inst = i.split()
    
    if inst[0] == 'rect':
        w, h = inst[1].split('x')
        w, h = int(w), int(h)
        screen[:h,:w] = True

    elif inst[0] == 'rotate':
        if inst[1] == 'column':
            c = int(inst[2].split('=')[1])
            s = int(inst[4])
            screen[:,c] = np.roll(screen[:,c], shift=s)

        elif inst[1] == 'row':
            r = int(inst[2].split('=')[1])
            s = int(inst[4])
            screen[r,:] = np.roll(screen[r,:], shift=s)

        else:
            sys.exit('error: rotate')
    else:
        sys.exit('error: inst')

print_screen()
print(number_of_on_pixels())
