#! python3

puzzle = "vzbxkghb"
test_puzzle = puzzle

def _has_straight(in_str):
    b = bytes(in_str, 'utf-8')
    for i in range(0, len(in_str)-2):
        if chr(b[i]) == chr(b[i+1] - 1) and chr(b[i]) == chr(b[i+2] - 2):
            return True
    return False

def _no_bad_letters(in_str):
    bad_letters = ["i", "o", "l"]
    for c in in_str:
        if c in bad_letters:
            return False
    return True

def _has_multiple_pairs(in_str):
    pair_counter = 0
    pair_letters = []
    i = 0
    for i in range(0, len(in_str)-1):
        if in_str[i] == in_str[i+1] and in_str[i] not in pair_letters:
            pair_counter += 1
            pair_letters.append(in_str[i])
    if pair_counter >= 2:
        return True
    return False

def check_rules(in_str):
    return _has_straight(in_str) and _no_bad_letters(in_str) and _has_multiple_pairs(in_str)

def increment_puzzle(in_str):
    a = in_str
    b = bytes(in_str, 'utf-8')
    check_index = len(in_str)
    while b[check_index-1] == 122:
        a = a[:check_index-1] + chr(97) + a[check_index:]
        b = bytes(a, 'utf-8')
        check_index -= 1
    a = a[:check_index-1] + chr(b[check_index-1] + 1) + a[check_index:]
    return a

#print(chr(97), chr(122))
print("puzzle is", puzzle)
password_counter = 1

while True:
    test_puzzle = increment_puzzle(test_puzzle)
    if check_rules(test_puzzle):
        print(password_counter, test_puzzle)
        password_counter += 1
        #break
