# Using readlines()
file1 = open('2022/01input.txt', 'r', encoding='utf-8')
Lines = file1.readlines()

current_elf = 1
current_calories = 0
calories = {}
for line in Lines:
    line = line.rstrip()
    if line == "":
        #print("next elf")
        calories[current_elf] = current_calories
        current_elf += 1
        current_calories = 0
        continue
    cal = int(line)
    current_calories += cal

calories_values = calories.values()
print("\npart1")
print(max(calories_values))

print("\npart2")
#print(sorted(zip(calories.values(), calories), reverse=True)[:3])
print(sum(sorted(calories_values, reverse=True)[:3]))
