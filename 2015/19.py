#! python3

molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

replacements = [] # list of tuples

result_molecules = set() # set

with open("./2015/19input", "r") as f:
    for line in f:
        line = line.replace("=> ", "")
        q, r = line.rstrip().split(" ")
        replacements.append((q, r))

# part 1

for q, r in replacements:
    for i in range(len(molecule)):
        if molecule[i:i+len(q)] == q:
            candidate = molecule[:i] + r + molecule[i+len(q):]
            result_molecules.add(candidate)
        
print(len(result_molecules))

# part 2
## with randomness from /u/What-A-Baller 
## https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/

from random import shuffle

target = molecule
steps = 0

while target != 'e':
    candidate = target
    for q, r in replacements:
        if r not in target:
            continue

        target = target.replace(r, q, 1)
        steps += 1

    # if no replacement was possible -> reset
    if candidate == target:
        target = molecule
        steps = 0
        shuffle(replacements)

print(steps)
