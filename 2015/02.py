#! python3

surface_area = 0
ribbon_length = 0

with open("02input") as f:
    for line in f:
        present = [int(x) for x in line.rstrip("\n\r").split("x")]
        l, w, h = present
        surface_area += (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, h*l)
        present.sort()
        ribbon_length += (present[0] + present[0] + present[1] + present[1]) + (l*w*h)

print(surface_area) # part 1
print(ribbon_length) # part 2
