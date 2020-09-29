#! python3 

with open("./2015/08input", "r") as f:
    raw_sum = 0
    cooked_sum = 0
    escaped_sum = 0
    for line in f:
        line = line.rstrip()
        raw_sum += len(line)
        cooked_sum += len(eval(line))
        escaped_sum += 2 + line.count("\\") + line.count('"')
    print(raw_sum, "-", cooked_sum, "=", raw_sum - cooked_sum)
    print(escaped_sum)
        