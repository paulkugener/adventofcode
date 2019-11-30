#! python3

def evaluate(target_gate, instructions, wires):
    try:
        wires[target_gate] = int(target_gate)
        return
    except ValueError:
        pass

    operation = instructions[target_gate]
    if len(operation) == 1: # (set value)
        try:
            wires[target_gate] = int(operation[0])
        except ValueError:
            evaluate(operation[0], instructions, wires)
            wires[target_gate] = wires[operation[0]]
    elif "NOT" in operation:
        if wires.get(operation[1]) is None:
            evaluate(operation[1], instructions, wires)
        wires[target_gate] = ~wires[operation[1]]
    elif len(operation) == 3:
        # left hand side = operation[0]
        # right hand side = operation[2]
        if wires.get(operation[0]) is None:
            evaluate(operation[0], instructions, wires)
        if wires.get(operation[2]) is None:
            evaluate(operation[2], instructions, wires)
        if "AND" in operation:
            wires[target_gate] = wires[operation[0]] & wires[operation[2]]
        elif "OR" in operation:
            wires[target_gate] = wires[operation[0]] | wires[operation[2]]
        elif "RSHIFT" in operation:
            wires[target_gate] = (wires[operation[0]] >> int(operation[2]))
        elif "LSHIFT" in operation:
            wires[target_gate] = (wires[operation[0]] << int(operation[2]))

if __name__ == "__main__":
    instructions = dict()
    wires = {}
    with open("07input") as f:
        for line in f:
            operation, target = line.split("->")
            instructions[target.strip()] = operation.strip().split(" ")
    evaluate('a', instructions, wires)
    print("part 1:", wires['a'])
    # part 2:
    wires = {'b': wires['a']}
    evaluate('a', instructions, wires)
    print("part 2:", wires['a'])

# Solutions:
# Wire [a] has the signal 3176 after running the circuit.
# Wire [a] has the signal 14710 after running the circuit.
