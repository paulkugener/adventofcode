#!/usr/bin/env python3
from collections import defaultdict

# Begin in state A.
# Perform a diagnostic checksum after 12172063 steps.
state = 'A'
pos = 0
tape = defaultdict(int)
steps = 12_172_063

for i in range(steps):
    if i % 1_000_000 == 0:
        progress = "{:.0%}".format(i/steps)
        print("running.. completed", progress)
    if pos not in tape.keys():
        tape[pos] = 0
    # In state A:
    #   If the current value is 0:
    #     - Write the value 1.
    #     - Move one slot to the right.
    #     - Continue with state B.
    #   If the current value is 1:
    #     - Write the value 0.
    #     - Move one slot to the left.
    #     - Continue with state C.
    if state == 'A':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'B'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'C'
        continue

    # In state B:
    #   If the current value is 0:
    #     - Write the value 1.
    #     - Move one slot to the left.
    #     - Continue with state A.
    #   If the current value is 1:
    #     - Write the value 1.
    #     - Move one slot to the left.
    #     - Continue with state D.
    elif state == 'B':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'A'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'D'
        continue

    # In state C:
    #   If the current value is 0:
    #     - Write the value 1.
    #     - Move one slot to the right.
    #     - Continue with state D.
    #   If the current value is 1:
    #     - Write the value 0.
    #     - Move one slot to the right.
    #     - Continue with state C.
    elif state == 'C':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'D'
        else:
            tape[pos] = 0
            pos += 1
            state = 'C'
        continue

    # In state D:
    #   If the current value is 0:
    #     - Write the value 0.
    #     - Move one slot to the left.
    #     - Continue with state B.
    #   If the current value is 1:
    #     - Write the value 0.
    #     - Move one slot to the right.
    #     - Continue with state E.
    elif state == 'D':
        if tape[pos] == 0:
            tape[pos] = 0
            pos -= 1
            state = 'B'
        else:
            tape[pos] = 0
            pos += 1
            state = 'E'
        continue

    # In state E:
    #   If the current value is 0:
    #     - Write the value 1.
    #     - Move one slot to the right.
    #     - Continue with state C.
    #   If the current value is 1:
    #     - Write the value 1.
    #     - Move one slot to the left.
    #     - Continue with state F.
    elif state == 'E':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'C'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'F'
        continue

    # In state F:
    #   If the current value is 0:
    #     - Write the value 1.
    #     - Move one slot to the left.
    #     - Continue with state E.
    #   If the current value is 1:
    #     - Write the value 1.
    #     - Move one slot to the right.
    #     - Continue with state A.
    elif state == 'F':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'E'
        else:
            tape[pos] = 1
            pos += 1
            state = 'A'
        continue

part1 = 0
for i in tape:
    part1 += tape[i]
print(part1)
