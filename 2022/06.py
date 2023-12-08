
def find_start_marker(s, l):
    i = 0
    while True:
        slice = s[i:i+l]
        #print(slice, set(slice), len(set(slice)))
        if len(set(slice)) == l:
            return i + l
        i = i + 1
    return -1

def main():
    with open('2022/06input') as file:
        lines = file.read().strip()
    datastream = lines
    answer1 = find_start_marker(datastream, 4)
    answer2 = find_start_marker(datastream, 14)
    print(f"{answer1 = }")
    print(f"{answer2 = }")

if __name__ == '__main__':
    exit(main())
