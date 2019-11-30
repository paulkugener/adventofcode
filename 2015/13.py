#! python3

with open('13input', 'r') as f:
    for line in f:
        guest, _, change, value, _, _, _, _, _, _, neighbor = line.split(' ')
        print(guest, change, value, neighbor)
        