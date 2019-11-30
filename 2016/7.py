#!/usr/bin/env python3
import re
import copy

def populate(node):
    sub_tree = {child_node: populate(child_node) for child_node in children[node]}
    child_full_weights = [full_weights[child_node] for child_node in children[node]]
    full_weights[node] = weights[node] + sum(child_full_weights)
    if len(set(child_full_weights)) > 1:
        target_weight = max(set(child_full_weights), key=child_full_weights.count)
        actual_weight = min(set(child_full_weights), key=child_full_weights.count)
        unbalanced[actual_weight] = weights[children[node][child_full_weights.index(actual_weight)]] + (target_weight - actual_weight)
    return sub_tree

tree, children, weights, unbalanced = {}, {}, {}, {}

for line in open("7input.txt", "r"):
    parts = re.split("\s\(|\)\s->\s|\)$", line.splitlines()[0])
    weights[parts[0]] = int(parts[1])
    children[parts[0]] = [word for word in (parts[2].split(", ") if parts[2] else [])]

full_weights = copy.deepcopy(weights)

for name in list(children.keys()):
    if name not in [word for children in children.values() for word in children]:
        tree[name] = populate(name)

print(list(tree.keys())[0])
print(unbalanced[min(unbalanced.keys())])
