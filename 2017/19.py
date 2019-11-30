#!/usr/bin/env python3

def day19(pipes):
    path = list()
    steps = 0

    y = 0
    x = pipes[y].find('|')
    orientation = 'S' # N, O, S, W
    current_case = pipes[y][x]

    while current_case != ' ':
        steps += 1
        if orientation == 'N':
            y -= 1
        elif orientation == 'O':
            x += 1
        elif orientation == 'S':
            y += 1
        elif orientation == 'W':
            x -= 1

        current_case = pipes[y][x]
        if current_case == '+':
            if orientation in ('N', 'S'):
                if pipes[y][x-1] != ' ':
                    orientation = 'W'
                else:
                    orientation = 'O'
            else:
                if pipes[y-1][x] != ' ':
                    orientation = 'N'
                else:
                    orientation = 'S'
        elif current_case not in ('|', '-'):
            path.append(current_case)
    return ''.join(path), steps


if __name__ == '__main__':
    with open('19input.txt') as f:
        input_ = f.readlines()

    print(day19(input_))
