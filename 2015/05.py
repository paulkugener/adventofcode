#! python3

def check_3_vowels(instr):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in instr:
        if char in vowels:
            count += 1
    if count >= 3:
        return True
    return False

def check_double_letters(instr):
    for index in range(0, len(instr)-1):
        if instr[index] == instr[index+1]:
            return True
    return False

def check_naughty_combinations(instr):
    naughty_combinations = ["ab", "cd", "pq", "xy"]
    for combination in naughty_combinations:
        if combination in instr:
            return False
    return True

def check_pair_without_overlap(instr):
    for index in range(0, len(instr)-1):
        if instr[index:index+2] in instr[index+2:]:
            #print(instr, instr[index:index+2], (instr[:index] + instr[index+2:])) #FALSE -> we dont need to check before our current pattern -> actually we are introducing errors by concatenating the sliced string 
            #print(instr, instr[index:index+2], instr[index+2:]) # correct
            return True
    return False

def check_repeat_with_skip(instr):
    for index in range(0, len(instr)-2):
        if instr[index] == instr[index+2]:
            #print(instr, instr[index], instr[index+2])
            return True
    return False

nice_counter_1 = 0
nice_counter_2 = 0

with open("./2015/05input") as f:
    for line in f:
        line = line.rstrip("\n\r")
        if  check_3_vowels(line) and check_double_letters(line) and check_naughty_combinations(line):
            nice_counter_1 += 1
        if check_pair_without_overlap(line) and check_repeat_with_skip(line):
            nice_counter_2 += 1

print(nice_counter_1)
print(nice_counter_2)
