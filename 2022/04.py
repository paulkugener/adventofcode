
def compute_fully_contain(pair):
    a, b = pair.split(',')
    a_start, a_end = a.split('-')
    b_start, b_end = b.split('-')
    a_range = range(int(a_start), int(a_end) + 1)
    b_range = range(int(b_start), int(b_end) + 1)
    if all(i in a_range for i in b_range) or all(j in b_range for j in a_range):
        return 1
    return 0

def compute_partly_contain(pair):
    a, b = pair.split(',')
    a_start, a_end = a.split('-')
    b_start, b_end = b.split('-')
    a_range = range(int(a_start), int(a_end) + 1)
    b_range = range(int(b_start), int(b_end) + 1)
    if any(i in a_range for i in b_range) or any(j in b_range for j in a_range):
        return 1
    return 0

def main():
    with open('2022/04input') as file:
        pair_list = [line.strip() for line in file]
        part1_score = 0
        part2_score = 0
        for p in pair_list:
            part1_score += compute_fully_contain(p)
            part2_score += compute_partly_contain(p)
        print('part1: {}'.format(part1_score))
        print('part2: {}'.format(part2_score))

if __name__ == '__main__':
    exit(main())
