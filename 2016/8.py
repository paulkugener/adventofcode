#!/usr/bin/env python3
from collections import defaultdict

registers = defaultdict(int)
max_part2 = 0

with open("8input.txt", "r") as f:
    for line in f:
        reg1, instr, num1, iff, reg2, op, num2 = line.split()
        if eval("registers[reg2]" + op + num2):
            if instr == 'inc':
                registers[reg1] += int(num1)
            else:
                registers[reg1] -= int(num1)
            max_part2 = max(max_part2, registers[reg1])


print(max(registers.values())) # part 1
print(max_part2) # part 2
