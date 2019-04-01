#!/usr/bin/env python3

with open('16input.txt') as f:
    instr = f.readline().split(',')

    progs = list("abcdefghijklmnop") # 16 progs
    reps = 1000000000

    part1 = True
    visited = list()
    for j in range(reps):
        s = ''.join(progs)
        if s in visited:
            # Now we found the first repetition in our dance
            # so we have cycles of length 'j'.
            # We calculate the remainder of 'reps / j' with modulo
            # And now we can tell in what order the programs will be at 'reps'
            print(visited[reps % j], j) # part2, len(cycle)
            break
        visited.append(s)

        for i in instr:
            if i[0] == 's': #spin
                dist = int(i[1:])
                progs = progs[-dist:] + progs[:-dist]
            elif i[0] == 'x': #exchange
                a, b = i[1:].split('/')
                a, b = int(a), int(b)
                progs[a], progs[b] = progs[b], progs[a]
            elif i[0] == 'p': #partner
                a, b = i[1:].split('/')
                a, b = progs.index(a), progs.index(b)
                progs[a], progs[b] = progs[b], progs[a]
        if part1:
            print(''.join(progs)) # part1
            part1 = False
