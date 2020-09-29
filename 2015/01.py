#! python3

level = 0
position = 0
basementFlag = False

with open("./2015/01input") as f:
    for line in f:
        for char in line:
            if char == "(":
                level += 1
            elif char == ")":
                level -= 1
            if basementFlag == False:
                position += 1
                if level < 0:
                    basementFlag = True

print(level) # 1
print(position) # 2
