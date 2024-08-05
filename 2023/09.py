
def p1(history):
    result = 0
    for h in history:
        result = result + compute_next_value(h)
    return result

def compute_next_value(h):
    h_detail = []
    h_detail.append(h)
    # compute all sequence of differences
    while not is_zero(h_detail[-1]):
        next_h = []
        h_1 = h_detail[-1]
        for i, x in enumerate(h_1[0:-1]):
            next_h.append(h_1[i+1] - h_1[i])
        h_detail.append(next_h)
    # extrapolate
    h_detail[-1].append(0)
    for s_index in range(len(h_detail) - 2, -1, -1):
        h_detail[s_index].append(h_detail[s_index][-1] + h_detail[s_index+1][-1])
    # print(h_detail)
    return h_detail[0][-1]

def p2(history):
    result = 0
    for h in history:
        result = result + compute_prev_value(h)
    return result

def compute_prev_value(h):
    h_detail = []
    h_detail.append(h)
    # compute all sequence of differences
    while not is_zero(h_detail[-1]):
        next_h = []
        h_1 = h_detail[-1]
        for i, x in enumerate(h_1[0:-1]):
            next_h.append(h_1[i+1] - h_1[i])
        h_detail.append(next_h)
    # extrapolate
    h_detail[-1].insert(0, 0)
    for s_index in range(len(h_detail) - 2, -1, -1):
        h_detail[s_index].insert(0, h_detail[s_index][0] - h_detail[s_index+1][0])
    # print(h_detail)
    return h_detail[0][0]

def is_zero(h):
    for n in h:
        if n != 0:
            return False
    return True

def main():
    with open('./2023/09input.txt') as file:
        lines = file.readlines()
    history = [[int(x) for x in line.split()] for line in lines]

    part1 = p1(history)
    print(f"{part1 = }")
    part2 = p2(history)
    print(f"{part2 = }")

if __name__ == '__main__':
    exit(main())
