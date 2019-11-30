#! python3

# https://www.geeksforgeeks.org/md5-hash-python/

import hashlib

secret_key = "iwrupvqb"
number = 1

while True:
    str_to_encode = secret_key + str(number)
    result = hashlib.md5(str_to_encode.encode()).hexdigest()
    if result.startswith("00000"):
        break
    number += 1

print(result)
print(number)


number = 1

while True:
    str_to_encode = secret_key + str(number)
    result = hashlib.md5(str_to_encode.encode()).hexdigest()
    if result.startswith("000000"):
        break
    number += 1

print(result)
print(number)
