#!/usr/bin/env python3
import collections

messages = []

with open("./2016/06input") as f:
    for line in f:
        line = line.rstrip()
        messages.append(line)

correct_message_1 = ''
correct_message_2 = ''

for i in range(0,8):
    tmp = ''
    for m in messages:
        tmp += m[i]
    res = collections.Counter(tmp)
    correct_message_1 += max(res, key = res.get)
    correct_message_2 += min(res, key = res.get)
    
print(correct_message_1)
print(correct_message_2)
