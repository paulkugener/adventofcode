#!/usr/bin/env python3
from operator import add

class Particle():
    def __init__(self, pid, pos, vel, acc):
        self.pid = pid
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def next(self):
        self.vel = list(map(add, self.vel, self.acc))
        self.pos = list(map(add, self.pos, self.vel))

    def distance(self):
        return int(abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2]))


def main():
    particles = list()
    with open('20input.txt') as f:
        i = 0
        for line in f:
            pos, vel, acc = line.split()
            pos = pos[pos.index('<')+1:pos.index('>')].split(',')
            pos = list(map(int, pos))
            vel = vel[vel.index('<')+1:vel.index('>')].split(',')
            vel = list(map(int, vel))
            acc = acc[acc.index('<')+1:acc.index('>')].split(',')
            acc = list(map(int, acc))
            p = Particle(i, pos, vel, acc)
            particles.append(p)
            i += 1

    for _ in range(500):
        for p in particles:
            p.next()
        part2 = True
        if part2:
            collisions = set()
            for pi in particles: # check for collisions
                for pj in particles:
                    if pi.pid != pj.pid and pi.pos == pj.pos:
                        collisions.add(pi)
                        collisions.add(pj)
            if collisions:
                for c in collisions:
                    particles.remove(c)
                print("removed collisions, we are left with {} particles"\
                    .format(len(particles))) # part 2

    min_distance = None
    min_pid = None
    for p in particles:
        if min_distance is None or p.distance() < min_distance:
            min_distance = p.distance()
            min_pid = p.pid

    print("particle {} is the closest with distance {}".format(min_pid,\
        min_distance)) # part 1

if __name__ == '__main__':
    main()
