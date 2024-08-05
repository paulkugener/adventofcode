from math import lcm

def travel(instructions, network):
    current = 'AAA'
    target = 'ZZZ'
    total_steps = 0
    i = 0
    while current != target:
        next = network[current][instructions[i]]
        i = i + 1
        if i == len(instructions):
            i = 0
        total_steps = total_steps + 1
        current = next
    return total_steps

def ghost_travel(instructions, network):
    # get all ghost starts
    ghost_starts = [k for k in network.keys() if k[2] == 'A']
    ghost_loops = []
    # travel 
    # - compute loop length and calculate 'Least common multiple'
    # - brute force is too expensive
    for node in ghost_starts:
        current_node = node
        total_steps = 0
        i = 0
        while not is_at_target(current_node):
            next_node = network[current_node][instructions[i]]
            i = i + 1
            if i == len(instructions):
                i = 0
            total_steps = total_steps + 1
            current_node = next_node
        ghost_loops.append(total_steps)
    # print(ghost_loops)
    return lcm(*ghost_loops)

def is_at_target(c):
    if c[2] != 'Z':
        return False
    return True

def main():
    with open('./2023/08input.txt') as file:
        lines = file.read()
    instructions, network_raw = lines.split("\n\n")
    network = dict()
    for l in network_raw.splitlines():
        k, target = l.split(' = ')
        left, right = target[1:-1].split(', ')
        network[k] = {
            'L': left,
            'R': right
        }
    part1 = travel(instructions, network)
    print(f"{part1 = }")
    part2 = ghost_travel(instructions, network)
    print(f"{part2 = }")

if __name__ == '__main__':
    exit(main())
