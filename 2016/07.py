#!/usr/bin/env python3
import re
import sys

ips = []

with open("./2016/07input") as f:
    for line in f:
        line = line.rstrip()
        ips.append(line)

# no ABBA in []
# AAAA != ABBA

def check_inside(j):
    k = 0
    while k < len(j)-3:
        if j[k] == j[k+3] and j[k+1] == j[k+2] and j[k] != j[k+1]:
            return False
        k += 1
    return True

def check_outside(j):
    k = 0
    while k < len(j)-3:
        if j[k] == j[k+3] and j[k+1] == j[k+2] and j[k] != j[k+1]:
            return True
        k += 1
    return False

def check_ip(a):
    result = False
    for j in range(len(a)):
        if j % 2 == 1:
            if check_inside(a[j]) == False:
                return False
        if j % 2 == 0:
            if check_outside(a[j]):
                result = True
    return result

def check_part2(a):
    outside = ''
    inside = ''
    for j in range(len(a)):
        if j % 2 == 0:
            outside += '.' + a[j]
        else:
            inside += ',' + a[j]
    
    k = 0
    while k < len(outside)-2:
        if outside[k] == outside[k+2] and outside[k] != outside[k+1] and outside[k+1] != '.':
            # ! you need to check for BAB, not ABA! :)
            if ''.join([outside[k+1], outside[k], outside[k+1]]) in inside:
                return True
        k += 1
    return False


checked = 0
result1 = 0
result2 = 0

for ip in ips:
    a = ip.replace('[', ':').replace(']', ':')
    a = a.split(':')
    if check_ip(a):
        result1 += 1
    if check_part2(a):
        result2 += 1
    checked += 1

print(len(ips), checked, result1, result2)
