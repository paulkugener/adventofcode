#! python3
import sys

p = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0"
p1 = "1,0,0,0,99"
p2 = "2,3,0,3,99"
p3 = "2,4,4,5,99,0"
p4 = "1,1,1,4,99,5,6,0,99"
p5 = "1,9,10,3,2,3,11,0,99,30,40,50"

# opcode
# 1 addition
# 2 multiplication
# 99 halt

def transform_to_list(str):
    return [int(x) for x in str.split(',')]

def do_operations(puzzle, noun=12, verb=2):
    intcode = transform_to_list(puzzle)
    intcode[1] = noun
    intcode[2] = verb
    for index in range(0, len(intcode), 4):
        if intcode[index] == 99:
            return intcode[0]
        elif intcode[index] == 1:
            intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]]
        elif intcode[index] == 2:
            intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]]
        else:
            return "error: opcode"

# To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

# part1
print(do_operations(p))

# part2
for a in range(100):
    for b in range(100):
        result = do_operations(p, a, b)
        if int(result) == 19690720:
            print(100 * a + b)
