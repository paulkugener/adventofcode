#!/usr/bin/python3

polymer = open('05input.in').read()

# react
def part1(polymer):
    _polymer = polymer
    i = 0
    while True:
        if i >= len(_polymer) - 1:
            break
        if _polymer[i].swapcase() == _polymer[i+1]:
            _polymer = _polymer[:i] + _polymer[i+2:]
            i -= 2
        i += 1
        if i < 0:
            i = 0
    return len(_polymer)

print("part 1 = " + str(part1(polymer)))

def part2(polymer):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    _polymer = polymer
    shortest = 50000
    for c in alpha:
        _p = _polymer.replace(c, '').replace(c.upper(), '')
        p_length = part1(_p)
        if p_length < shortest:
            shortest = p_length
    return shortest

print("part 2 = " + str(part2(polymer)))
