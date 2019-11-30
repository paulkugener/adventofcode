#! python3

from itertools import groupby

puzzle = "1321131112"

def look_and_say(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string

if __name__ == "__main__":
    print(len(look_and_say(puzzle, 40)))
    print(len(look_and_say(puzzle, 50)))
