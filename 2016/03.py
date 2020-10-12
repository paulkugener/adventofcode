#!/usr/bin/env python3
import sys

triangles = []
with open("./2016/03input") as f:
    for line in f:
        line_list = line.rstrip().split()
        triangles.append([int(x) for x in line_list])

result1 = 0

for tri in triangles:
    if tri[0]+tri[1]>tri[2] and tri[1]+tri[2]>tri[0] and tri[2]+tri[0]>tri[1]:
        result1 += 1

print(result1)

result2 = 0

for i in range(0, len(triangles)-1, 3):
    for j in range(3):
        if triangles[i][j]+triangles[i+1][j]>triangles[i+2][j] and triangles[i+1][j]+triangles[i+2][j]>triangles[i][j] and triangles[i+2][j]+triangles[i][j]>triangles[i+1][j]:
            result2 += 1

print(result2)
