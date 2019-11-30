#!/usr/bin/python3

with open("02input.in", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Part 1: count 2x &/ 3x same character
two_counter = 0
three_counter = 0
for item in data:
    two_flag = False
    three_flag = False
    for c in item:
        if item.count(c) == 2:
            two_flag = True
        if item.count(c) == 3:
            three_flag = True
    if two_flag:
        two_counter += 1
    if three_flag:
        three_counter += 1

print("part 1 solution = " + str(two_counter * three_counter))

# Part 2
for i in data:
    for j in data:
        diffs = 0
        for idx, ch in enumerate(i):
            if ch != j[idx]:
                diffs += 1
        if diffs == 1:
            ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
            print("part 2 solution = ", ''.join(ans))
            break
