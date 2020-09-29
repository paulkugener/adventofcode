#! python3

lower_bound, upper_bound = 234208, 765869

def has_adjacent(number):
    index = 0
    n = str(number)
    for index in range(0, len(n) - 1):
        if n[index] == n[index+1]:
            return True
    return False

def only_increase(number):
    index = 0
    n = str(number)
    for index in range(0, len(n) - 1):
        if n[index] > n[index+1]:
            return False
    return True

def check_criteria1(number):
    return has_adjacent(number) and only_increase(number)

assert check_criteria1(11111) == True
assert check_criteria1(223450) == False
assert check_criteria1(123789) == False
assert check_criteria1(122345) == True

possible_passwords1 = list()

for i in range(lower_bound, upper_bound):
    if check_criteria1(i):
        possible_passwords1.append(i)

print(len(possible_passwords1))

def has_strict_double_adjacent(number):
    n = str(number)
    for c in n:
        if n.count(c) == 2:
            return True
    return False

def check_criteria2(number):
    return has_strict_double_adjacent(number) and has_strict_double_adjacent(number) and only_increase(number)

assert check_criteria2(112233) == True
assert check_criteria2(123444) == False
assert check_criteria2(111122) == True

possible_passwords2 = list()

for i in range(lower_bound, upper_bound):
    if check_criteria2(i):
        possible_passwords2.append(i)

print(len(possible_passwords2))
