#! python3

import json

data = json.loads(open('./2015/12input', 'r').read())

def sum_numbers(obj):
    if type(obj) == type(dict()):
        #if "red" in obj.values(): # use this for part 2
        #    return 0
        return sum(map(sum_numbers, obj.values()))

    if type(obj) == type(list()):
        return sum(map(sum_numbers, obj))

    if type(obj) == type(0):
        return obj

    return 0

print(sum_numbers(data))
