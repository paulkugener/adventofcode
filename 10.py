#!/usr/bin/env python3

number_list = list(range(0, 256))
#number_list = list(range(0, 5)) # for test
curr_pos = 0
skip_size = 0
lengths = [88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205]
#lengths = [3,4,1,5] # for test

for l in lengths:
    # Reverse the order of that length of elements in the list,
    # starting with the element at the current position.
    sub_list = list()
    for x in range(l):
        i = (curr_pos + x) % len(number_list)
        sub_list.append(number_list[i])
    sub_list.reverse()
    for x in range(l):
        i = (curr_pos + x) % len(number_list)
        number_list[i] = sub_list[x]
    # Move the current position forward by that length plus the skip size.
    curr_pos += l + skip_size
    curr_pos = curr_pos % len(number_list)
    # Increase the skip size by one.
    skip_size += 1

print(number_list[0] * number_list[1]) # part 1


# ================== part 2 ===================
from functools import reduce
from operator import xor

number_list = list(range(0, 256))
curr_pos = 0
skip_size = 0
lengths = [ord(x) for x in "88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205"]
lengths.extend([17, 31, 73, 47, 23])

for _ in range(64):
    for l in lengths:
        # Reverse the order of that length of elements in the list,
        # starting with the element at the current position.
        sub_list = list()
        for x in range(l):
            i = (curr_pos + x) % len(number_list)
            sub_list.append(number_list[i])
        sub_list.reverse()
        for x in range(l):
            i = (curr_pos + x) % len(number_list)
            number_list[i] = sub_list[x]
        # Move the current position forward by that length plus the skip size.
        curr_pos += l + skip_size
        curr_pos = curr_pos % len(number_list)
        # Increase the skip size by one.
        skip_size += 1

dense_hash = list()
for x in range(0, 16):
    sub_list = number_list[16*x:16*x+16]
    dense_hash.append('%02x'%reduce(xor, sub_list))

print(''.join(dense_hash)) # part 2
