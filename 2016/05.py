#!/usr/bin/env python3
import hashlib
import sys

# https://www.geeksforgeeks.org/md5-hash-python/
#   --> string - hexadecimal

puzzle_input = 'ugkcyxxp'
test_input = 'abc'
index = 0


# part 1
password = ''

while len(password) != 8:
    code = puzzle_input + str(index)
    tmp = hashlib.md5(code.encode())
    tmp_result = tmp.hexdigest()
    if tmp_result.startswith('00000'):
        password += tmp_result[5]
    index += 1

print("part 1", password)

# part 2
index = 0
password = [None, None, None, None, None, None, None, None]

while None in password:
    code = puzzle_input + str(index)
    tmp = hashlib.md5(code.encode())
    tmp_result = tmp.hexdigest()
    if tmp_result.startswith('00000'):
        if tmp_result[5].isdigit():
            if 0 <= int(tmp_result[5]) <= 7 and password[int(tmp_result[5])] == None:
                password[int(tmp_result[5])] = tmp_result[6]
    index += 1

print("part 2", "".join(password))
