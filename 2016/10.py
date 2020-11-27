#!/usr/bin/env python3
import collections

instructions = []

with open("./2016/10input") as f:
    for line in f:
        line = line.rstrip()
        instructions.append(line)

bot = collections.defaultdict(list)
output = collections.defaultdict(list)
pipeline = {}

for line in instructions:
    if line.startswith('value'):
        # value 43 goes to bot 90
        _, num, _, _, _, b = line.split()
        bot[int(b)].append(int(num))
    if line.startswith('bot'):
        # bot 152 gives low to bot 155 and high to bot 70
        _, source, _, _, _, type_lo, dest_lo, _, _, _, type_hi, dest_hi = line.split()
        pipeline[int(source)] = (type_lo, int(dest_lo)), (type_hi, int(dest_hi))

while bot:
    for key, values in dict(bot).items():
        if len(values) == 2:
            v_lo, v_hi = sorted(bot.pop(key))
            if v_lo == 17 and v_hi == 61:
                print("part1", key)
            (type_lo, dest_lo), (type_hi, dest_hi) = pipeline[key]
            # my variant
            if type_lo == 'bot':
                bot[dest_lo].append(v_lo)
            elif type_lo == 'output':
                output[dest_lo].append(v_lo)
            if type_hi == 'bot':
                bot[dest_hi].append(v_hi)
            elif type_hi == 'output':
                output[dest_hi].append(v_hi)
            # pretty variant from /u/fatpollo https://www.reddit.com/r/adventofcode/comments/5hijk5/2016_day_10_solutions/
            # eval(type_lo)[dest_lo].append(v_lo)
            # eval(type_hi)[dest_hi].append(v_hi)

print("part2", output[0][0]*output[1][0]*output[2][0])
