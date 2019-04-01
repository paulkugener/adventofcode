#!/usr/bin/env python3

fstr = open("9input.txt", "r").readline()

curr_level = 0
score = 0
garbage = False
garbage_counter = 0

i = 0
while True:
    if i >= len(fstr):
        break
    if garbage:
        if fstr[i] == '!':
            i += 1
        elif fstr[i] == '>':
            garbage = False
        else:
            garbage_counter += 1
    elif fstr[i] == '{':
        curr_level += 1
        score += curr_level
    elif fstr[i] == '<':
        garbage = True
    elif fstr[i] == '}':
        curr_level -= 1
    i += 1

print(score)
print(garbage_counter)
