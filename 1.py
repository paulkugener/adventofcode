#!/usr/bin/env python3

f = open("1input.txt", "r")
fline = f.readline()
result = 0

for i in range(len(fline)):
    if fline[i] == fline[i-1]: # fline[0-1] == fline[-1] == last item of list
        result += int(fline[i])

print(result) #solution1 = 1119

# ------------------------------

result = 0

j = int(len(fline) / 2) # j starts as center index of fline
for i in range(len(fline)):
    if fline[i] == fline[j]:
        result += int(fline[i])
    j += 1
    if j == len(fline):
        j = 0

print(result) #solution2 = 1420
