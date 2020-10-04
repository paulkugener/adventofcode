#! python3
from pprint import pprint
import sys

# a, b = 0, 0 # if part 1
a, b = 1, 0 # if part 2 
instructions = []

with open("./2015/23input", "r") as f:
    for line in f:
        line = line.replace(",", "")
        i = line.rstrip().split(" ")
        instructions.append(i)

current_index = 0
while -1 < current_index < len(instructions):
    instr = instructions[current_index]

    if instr[0] == 'hlf':
        if instr[1] == 'a':
            a = a/2
        elif instr[1] == 'b':
            b = b/2
        current_index += 1
    
    elif instr[0] == 'tpl':
        if instr[1] == 'a':
            a = a*3
        elif instr[1] == 'b':
            b = b*3
        current_index += 1

    elif instr[0] == 'inc':
        if instr[1] == 'a':
            a += 1
        elif instr[1] == 'b':
            b += 1
        current_index += 1

    elif instr[0] == 'jmp':
        current_index += int(instr[1])

    elif instr[0] == 'jie':
        if instr[1] == 'a':
            if a % 2 == 0:
                current_index += int(instr[2])
            else: 
                current_index += 1
        elif instr[1] == 'b':
            if b % 2 == 0:
                current_index += int(instr[2])
            else: 
                current_index += 1

    elif instr[0] == 'jio':
        if instr[1] == 'a':
            if a == 1:
                current_index += int(instr[2])
            else: 
                current_index += 1
        elif instr[1] == 'b':
            if b == 1:
                current_index += int(instr[2])
            else: 
                current_index += 1

    else:
        sys.exit('Instruction unkown!')


print("a", a)
print("b", b)
