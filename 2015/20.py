#! python3
import numpy as np

puzzle = 36_000_000 # = target

CEILING = 1_000_000
houses1 = np.zeros(CEILING)
houses2 = np.zeros(CEILING)

for elf in range(1, CEILING):
    houses1[elf::elf] += elf * 10
    houses2[elf:elf+(elf*50):elf] += elf * 11

for k, v in np.ndenumerate(houses1):
    if v >= puzzle:
        print(k,v)
        break

for k, v in np.ndenumerate(houses2):
    if v >= puzzle:
        print(k,v)
        break
