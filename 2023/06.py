import sys

def get_winners(time, distance):
    winners = []
    for ms in range(time):
        speed = ms
        travel_time = time - ms
        my_distance = speed * travel_time
        if my_distance > distance:
            winners.append(ms)
    return len(winners)

def main():
    with open('./2023/06input.txt') as f:
        input_lines = f.read().splitlines()
    time = [int(x) for x in input_lines[0].split(':')[1].strip().split()]
    dist = [int(x) for x in input_lines[1].split(':')[1].strip().split()]

    winners = 1
    for i in range(len(time)):
        winners *= get_winners(time[i], dist[i])
    part1 = winners
    print(f"{part1 = }")

    time = int(''.join([str(t) for t in time]))
    dist = int(''.join([str(d) for d in dist]))
    part2 = get_winners(time, dist)
    print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
