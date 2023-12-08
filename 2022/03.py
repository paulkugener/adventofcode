
def get_wrong_type(rucksack):
    pivot = int(len(rucksack) / 2)
    first_compartment = rucksack[:pivot]
    second_compartment = rucksack[pivot:]
    return ''.join(set(first_compartment).intersection(set(second_compartment)))

def compute_priority(type):
    o = ord(type)
    if o > 96:
        return o - 96
    return o - 38

def compute_wrong_type_priority(rucksack):
    wrong_type = get_wrong_type(rucksack)
    return compute_priority(wrong_type)

def get_group_badge(r0, r1, r2):
    return ''.join(set(r0).intersection(set(r1)).intersection(set(r2)))

def compute_group_type_priority(r0, r1, r2):
    group_badge = get_group_badge(r0, r1, r2)
    return compute_priority(group_badge)

def main():
    with open('2022/03input') as file:
        rucksack_list = [line.strip() for line in file]
        part1_score = 0
        part2_score = 0
        for r in rucksack_list:
            part1_score += compute_wrong_type_priority(r)
        for i in range(0, len(rucksack_list), 3):
            part2_score += compute_group_type_priority(rucksack_list[i], rucksack_list[i+1], rucksack_list[i+2])
        print('part1: {}'.format(part1_score))
        print('part2: {}'.format(part2_score))

if __name__ == '__main__':
    exit(main())
