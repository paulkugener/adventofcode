#!/usr/bin/env python3
import copy, sys

instructions = list()

with open("./2020/08input") as f:
    for line in f:
        op, arg = line.strip().split()
        instructions.append((op, int(arg)))
     

def part1():
    # Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
    visited = set()
    accumulator = 0
    index = 0
    
    while True:
        visited.add(index)
        op, arg = instructions[index]
        if op == 'acc':
            accumulator += arg
            index += 1
        elif op == 'jmp':
            index += arg
        elif op == 'nop':
            index += 1
        if index in visited:
            break
    return accumulator


def part2():
    # Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
    GOAL = len(instructions)

    for i in range(GOAL):
        _op, _arg = instructions[i]
        if _op == 'acc':
            continue
        elif _op == 'jmp':
            _op = 'nop'
        elif _op == 'nop':
            _op = 'jmp'
        _instructions = copy.deepcopy(instructions)
        _instructions[i] = (_op, _arg)

        visited = set()
        accumulator = 0
        index = 0

        while True:
            visited.add(index)
            op, arg = _instructions[index]
            if op == 'acc':
                accumulator += arg
                index += 1
            elif op == 'jmp':
                index += arg
            elif op == 'nop':
                index += 1
            if index in visited:
                break
            if index == GOAL:
                return accumulator
    return -1


print(part1())
print(part2())
