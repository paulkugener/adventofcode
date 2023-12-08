
def build_dict(instructions):
    d = {
        '/home': 0
    }
    current_path = ''
    for i in instructions:
        w = i.strip().split(' ')
        match w[0]:
            case '$':
                # travel
                match w[1]:
                    case 'cd':
                        match w[2]:
                            case '/':
                                current_path = '/home'
                            case '..':
                                current_path = current_path[:current_path.rindex('/')]
                            case _:
                                current_path = current_path + '/' + w[2]
                                d[current_path] = 0
                    case _:
                        pass
            case 'dir':
                pass
            case _:
                # add file size to current folder
                tmp_path = current_path
                while tmp_path != '':
                    d[str(tmp_path)] += int(w[0])
                    tmp_path = tmp_path[:tmp_path.rindex('/')]
    return d

def answer_1(d):
    answer1 = 0
    for k, v in d.items():
        if v < 100_000:
            answer1 = answer1 + v
    print(f"{answer1 = }")

def answer_2(d):
    DISK_SPACE = 70_000_000
    NEEDED_SPACE = 30_000_000
    unused_space = DISK_SPACE - d['/home']
    target_freeup_space = NEEDED_SPACE - unused_space
    candidates = []
    for k, v in d.items():
        if v > target_freeup_space:
            candidates.append(v)
    print('answer2 =', min(candidates))

def main():
    with open('2022/07input') as file:
        lines = file.read().strip()
    instructions = lines.split("\n")
    d = build_dict(instructions)
    answer_1(d)
    answer_2(d)

if __name__ == '__main__':
    exit(main())
