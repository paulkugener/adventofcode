#!/usr/bin/env python3
from collections import defaultdict

def part1(instr):
    register = defaultdict(int)
    i = 0
    mul_counter = 0
    
    def val(v):
        try:
            return int(v)
        except ValueError:
            return register[v]

    while i < len(instr):
        op, x, y = instr[i].rstrip().split()
        if op == 'set':
            register[x] = val(y)
        elif op == 'sub':
            register[x] -= val(y)
        elif op == 'mul':
            register[x] *= val(y)
            mul_counter += 1
        elif op == 'jnz' and val(x) != 0:
            i += val(y)
            continue
        i += 1
    return mul_counter


def part2():

    def isprime(n):
        """Returns True if n is prime."""
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= n:
            if n % i == 0:
                return False

            i += w
            w = 6 - w

        return True

    b = 109900
    c = 126900
    h = 0

    for b in range(109900, c + 1, 17):
        if not isprime(b):
            h += 1

    return h

if __name__ == '__main__':
    with open('23input.txt') as f:
        input_ = f.read().splitlines()

    #print(part1(input_))
    print(part2())
