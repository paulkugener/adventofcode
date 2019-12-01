#! python3
import math
import pathlib

# divide by 3, round down, subtract 2

fuel = 0
PART2 = True

with open(pathlib.Path(__file__).parent / "01puzzle") as f:
    for line in f:
        mass = int(line.rstrip())
        fuel_tmp = math.floor(mass/3) - 2
        fuel += fuel_tmp
        if PART2:
            fuel_fuel = 0
            while((math.floor(fuel_tmp/3) - 2) > 0):
                fuel_tmp = math.floor(fuel_tmp/3) - 2
                fuel_fuel += fuel_tmp
            fuel += fuel_fuel

print(fuel)
