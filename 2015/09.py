#! python3

from itertools import permutations

distance_matrix = dict()
locations = set()

with open("./2015/09input", "r") as f:
    for line in f:
        from_location, _, to_location, _, distance = line.rstrip().split(" ")
        distance_matrix.setdefault(from_location, dict())[to_location] = int(distance)
        distance_matrix.setdefault(to_location, dict())[from_location] = int(distance)
        locations.add(from_location)
        locations.add(to_location)

shortest = 99999999999999
longest = 0
for items in permutations(locations):
    dist = sum(map(lambda x, y: distance_matrix[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest:", shortest)
print("longest:", longest)
