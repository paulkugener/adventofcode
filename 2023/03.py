import sys
from math import prod

def sum_part_numbers(schematic):
    return sum(get_part_numbers(schematic))

def get_part_numbers(s):
    valid_numbers = []
    i = 0
    while i < len(s):
        # print(s[i])
        j = 0
        while j < len(s[i]):
            if s[i][j].isdigit():
                jj = j+1
                while jj < len(s[i]):
                    if s[i][jj].isdigit() == False:
                        break
                    jj = jj+1
                candidate = ''.join(s[i][j:jj])
                # print(candidate)
                if is_valid(s, i, j, jj):
                    valid_numbers.append(int(candidate))
                j = jj
            j += 1
        i += 1
    return valid_numbers

def is_valid(s, i, j, jj):
    # print(f"{i=}, {j=}, {jj=}")
    neighbors_coord = set()
    cc = [(i, jjj) for jjj in range(j, jj)]
    for i_ in [i-1, i, i+1]:
        for j_ in range(j-1, jj+1):
            if i_ > -1 and i_ < len(s) and j_ > -1 and j_ < len(s[i_]) and (i_, j_) not in cc:
                # not out of range AND not candidate coordinates
                neighbors_coord.add((i_, j_))
    # print(f"{neighbors_coord =}")
    neighbors = set()
    for (y, x) in neighbors_coord:
        neighbors.add(s[y][x])
    # print(f"{neighbors =}")
    for char in neighbors:
        if char.isdigit() == False and char != '.':
            # print(char)
            return True
    return False

def sum_gear_ratios(schematic):
    return sum(get_gear_ratios(schematic))

def get_gear_ratios(s):
    gear_ratios = []
    i = 0
    while i < len(s):
        # print(s[i])
        j = 0
        while j < len(s[i]):
            if s[i][j] == '*':
                gear_ratios.append(find_gear_ratio(s, i, j))
            j += 1
        i += 1
    return gear_ratios

def find_gear_ratio(s, i, j):
    gear_candidates = []
    visited_coords = set()
    for ii in [i-1, i, i+1]:
        for jj in [j-1, j, j+1]:
            if (ii, jj) not in visited_coords:
                if s[ii][jj].isdigit():
                    jj_start = jj_end = jj
                    # find start
                    while jj_start > -1:
                        visited_coords.add((ii, jj_start))
                        if s[ii][jj_start-1].isdigit():
                            jj_start -= 1
                        else:
                            break
                    # find end
                    while jj_end < len(s[ii])-1:
                        visited_coords.add((ii, jj_end))
                        if s[ii][jj_end+1].isdigit():
                            jj_end += 1
                        else:
                            break
                    # commit
                    # print(s[ii][jj_start:jj_end+1])
                    gear_candidates.append(int(''.join(s[ii][jj_start:jj_end+1])))
            visited_coords.add((ii, jj))
    if len(gear_candidates) == 2:
        return prod(gear_candidates)
    return 0



def main():
    with open('./2023/03input.txt') as f:
        lines = f.read().splitlines()
    schematic = [[*line] for line in lines]
    part1 = sum_part_numbers(schematic)
    part2 = sum_gear_ratios(schematic)
    print(f"{part1 = }")
    print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
