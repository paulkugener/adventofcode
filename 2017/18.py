#!/usr/bin/env python3
from collections import defaultdict

def part1(instr):
    register = defaultdict(int)
    last_frequency = 0
    i = 0

    def val(v):
        try:
            return int(v)
        except ValueError:
            return register[v]

    while i < len(instr):
        line = instr[i].rstrip().split()
        if line[0] == 'snd':
            last_frequency = int(register[line[1]])
        elif line[0] == 'set':
            register[line[1]] = val(line[2])
        elif line[0] == 'add':
            register[line[1]] += val(line[2])
        elif line[0] == 'mul':
            register[line[1]] *= val(line[2])
        elif line[0] == 'mod':
            register[line[1]] %= val(line[2])
        elif line[0] == 'rcv':
            if register[line[1]] != 0:
                return last_frequency
        elif line[0] == 'jgz' and register[line[1]] > 0:
            i += val(line[2])
            continue
        i += 1


def part2(instr):
    p0 = Program(0, None, instr)
    p1 = Program(1, p0, instr)
    p0.other = p1

    while not ((p0.terminated or p0.blocked) and (p1.terminated or p1.blocked)):
        p0.next()
        p1.next()

    return p1.sent

class Program:
    def __init__(self, pid, other, instr):
        self.regs = defaultdict(int)
        self.regs['p'] = pid
        self.other = other
        self.instr = instr

        self.ip = 0
        self.buffer = []
        self.terminated = False
        self.blocked = False
        self.sent = 0

    def next(self):
        if self.terminated or self.ip < 0 or self.ip >= len(self.instr):
            self.terminated = True
            return
        ins = self.instr[self.ip].split()
        if ins[0] == 'snd':
            self.other.buffer.append(self.get(ins[1]))
            self.other.blocked = False
            self.sent += 1
        elif ins[0] == 'set':
            self.regs[ins[1]] = self.get(ins[2])
        elif ins[0] == 'add':
            self.regs[ins[1]] += self.get(ins[2])
        elif ins[0] == 'mul':
            self.regs[ins[1]] *= self.get(ins[2])
        elif ins[0] == 'mod':
            self.regs[ins[1]] %= self.get(ins[2])
        elif ins[0] == 'rcv':
            if len(self.buffer) > 0:
                self.regs[ins[1]] = self.buffer.pop(0)
            else:
                self.blocked = True
                return
        elif ins[0] == 'jgz':
            if self.get(ins[1]) > 0:
                self.ip += self.get(ins[2])
                return
        self.ip += 1

    def get(self, v):
        try:
            return int(v)
        except ValueError:
            return self.regs[v]


if __name__ == '__main__':
    with open('18input.txt') as f:
        input_ = f.read().splitlines()

    #print(part1(input_))
    print(part2(input_))
