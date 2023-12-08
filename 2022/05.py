from collections import defaultdict

def parse_state(string):
    state = defaultdict(list)
    start_state = [e for e in string.splitlines()]
    stack_ids = start_state[-1]
    for stack_id in stack_ids:
        if stack_id == ' ':
            continue
        stack_x = stack_ids.index(stack_id)
        stack_y = len(start_state)-2
        while stack_y >= 0:
            if start_state[stack_y][stack_x] == ' ':
                break
            state[stack_id].append(start_state[stack_y][stack_x])
            stack_y = stack_y - 1
    return state

def compute_instructions_9000(state, instructions):
    # move 2 from 2 to 1
    my_state = state
    instructions = [l for l in instructions.splitlines()]
    for l in instructions:
        _, amout, _, origin, _, destination = l.split(' ')
        for _ in range(int(amout)):
            if my_state[origin]:
                item = my_state[origin].pop()
                #print('item', item, 'origin', origin, 'destination', destination)
                my_state[destination].append(item)
    return my_state

def compute_instructions_9001(state, instructions):
    # move 2 from 2 to 1
    my_state = state
    instructions = [l for l in instructions.splitlines()]
    for l in instructions:
        _, amout, _, origin, _, destination = l.split(' ')
        if my_state[origin]:
            last_items = my_state[origin][-int(amout):]
            del my_state[origin][-int(amout):]
            my_state[destination].extend(last_items)
    return my_state

def print_top_items(description, state):
    result = []
    for k,v in state.items():
        result.append(v.pop())
    print(description + ' : ' + ''.join(result))

def main():
    with open('2022/05input') as file:
        lines = file.read()
    start_state, instructions = lines.split("\n\n")
    state1 = parse_state(start_state)
    state2 = parse_state(start_state)
    state1 = compute_instructions_9000(state1, instructions)
    print_top_items('state1', state1)
    state2 = compute_instructions_9001(state2, instructions)
    print_top_items('state2', state2)

if __name__ == '__main__':
    exit(main())
