#! python3

import re
re_d = re.compile(r'((\d)\2*)')

def replace(match_obj):
    s = match_obj.group(1)
    return str(len(s)) + s[0]

puzzle = '1321131112'
for i in range(50):
    puzzle = re_d.sub(replace,puzzle)
print(len(puzzle))
