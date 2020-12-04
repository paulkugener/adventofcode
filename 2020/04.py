#!/usr/bin/env python3
import copy, re, sys

passports = []

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) [optional for part1]

with open("./2020/04input") as f:
    p = {} # the one current passport
    for line in f:
        if line == '\n':
            passports.append(p)
            p = {}
        tmp = line.strip().split()
        for pair in tmp:
            k, v = pair.split(':')
            p[k] = v
    passports.append(p) # we need this for the last passport from the input
     
        
def part1(passports):
    # Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
    REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    result = 0
    for p in passports:
        keys = list(p.keys())
        # check if list 'keys' contains all elements of list 'REQUIRED1'
        valid = all(item in keys for item in REQUIRED)
        #print(keys, valid)
        if valid:
            result += 1
    return result

def part2(passports):
    # Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
    REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    result = 0
    for p in passports:
        keys = list(p.keys())
        present = all(item in keys for item in REQUIRED)
        if not present:
            continue
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not p['byr'].isnumeric():
            continue
        v = int(p['byr'])
        if not 1920 <= v <= 2002:
            continue
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not p['iyr'].isnumeric():
            continue
        v = int(p['iyr'])
        if not 2010 <= v <= 2020:
            continue
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not p['eyr'].isnumeric():
            continue
        v = int(p['eyr'])
        if not 2020 <= v <= 2030:
            continue
        # hgt (Height) - a number followed by either cm or in:
        v = p['hgt']
        num = v[:-2]
        metric = v[-2:]
        if not num.isnumeric():
            continue
        if metric not in ['cm', 'in']:
            continue
        num = int(num)
        #     If cm, the number must be at least 150 and at most 193.
        if metric == 'cm':
            if not 150 <= num <= 193:
                continue
        #     If in, the number must be at least 59 and at most 76.
        if metric == 'in':
            if not 59 <= num <= 76:
                continue
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        v = p['hcl']
        if not re.match(r"#[0-9a-f]{6}", v):
            continue
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        v = p['ecl']
        if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        v = p['pid']
        if len(v) != 9:
            # the following regex check does allow for a longer sequence of 9-digit numbers... for example a 10-digit number is also a 9-digit number... LIMIT the length!
            continue
        if not re.match(r"[0-9]{9}", v):
            continue
        # OKAY: if we arrive here, the passport is considered valid!
        result += 1
    return result


print(part1(passports))
print(part2(passports))
