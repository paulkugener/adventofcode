#!/usr/bin/env python3
import re, collections
import sys

rooms = []
regex = r'([a-z-]+)(\d+)\[(\w+)\]'

with open("./2016/04input") as f:
    for line in f:
        line = line.rstrip()
        for code, sid, checksum in re.findall(regex, line):
            code = code.replace('-', '')
            sid = int(sid)
            t = (code, sid, checksum)
            rooms.append(t)

result1 = 0

for (code, sid, checksum) in rooms:
    sorted_code = ''.join(sorted(code))
    top_letters = ''.join([t[0] for t in collections.Counter(sorted_code).most_common(5)])
    if top_letters == checksum:
        result1 += sid
        # part2
        #decript room name
        name = ''.join(chr((ord(char) - 97 + sid) % 26 + 97) for char in code)
        if 'north' in name:
            print(sid, name)

print(result1)
