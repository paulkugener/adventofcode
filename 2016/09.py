#!/usr/bin/env python3

# source /u/blockingthesky
# https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/

#puzzle = '(27x12)(20x12)(13x14)(7x10)(1x12)A'

puzzle = open('./2016/09input').read().strip()

part2 = False

def decompress(s):
    if '(' not in s:
        return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        if part2:
            ret += decompress(s[:int(marker[0])]) * int(marker[1])
        else:
            ret += len(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    ret += len(s)
    return ret

print(decompress(puzzle))
part2 = True
print(decompress(puzzle))
