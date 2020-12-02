#!/usr/bin/env python3
import sys

pw_list = []
with open("./2020/02input") as f:
    for line in f:
        r, l, p = line.split()
        lo, hi = r.split('-')
        lo, hi = int(lo), int(hi)
        l = l[0]
        t = (lo, hi, l, p)
        pw_list.append(t)

def part1(pw_list):
    result = 0
    for t in pw_list:
        (lo, hi, l, p) = t
        occ = p.count(l)
        if lo <= occ <= hi:
            result += 1
    return result

def part2(pw_list):
    result = 0
    for t in pw_list:
        (lo, hi, l, p) = t
        lo, hi = lo-1, hi-1
        if p[lo] == l and p[hi] != l or p[lo] != l and p[hi] == l: #Exactly one
            result += 1
    return result

print(part1(pw_list))
print(part2(pw_list))
