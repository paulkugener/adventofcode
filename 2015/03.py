#! python3

x, y = 0, 0
visits = [(x,y)]

with open("03input") as f:
    for line in f:
        for instruction in line:
            if instruction == "^":
                y += 1
            elif instruction == ">":
                x += 1
            elif instruction == "v":
                y -= 1
            elif instruction == "<":
                x -= 1
            visits.append((x,y))

unique_visits = set(visits)
print(len(unique_visits))

# ===================================

x, y = 0, 0
r_x, r_y = 0, 0

visits = [(x,y)]
r_visits = [(x,y)]
robo_flag = False

with open("03input") as f:
    for line in f:
        for instruction in line:
            if robo_flag == False:
                if instruction == "^":
                    y += 1
                elif instruction == ">":
                    x += 1
                elif instruction == "v":
                    y -= 1
                elif instruction == "<":
                    x -= 1
                visits.append((x,y))
            else:
                if instruction == "^":
                    r_y += 1
                elif instruction == ">":
                    r_x += 1
                elif instruction == "v":
                    r_y -= 1
                elif instruction == "<":
                    r_x -= 1
                r_visits.append((r_x,r_y))
            robo_flag = not robo_flag

u_visits = set(visits)
r_u_visits = set(r_visits)
uniquest_visits = u_visits.union(r_u_visits)
print(len(uniquest_visits))
