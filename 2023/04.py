import sys

def interpret_lines(lines):
    card_dict = {}
    for line in lines:
        card_info, numbers_str = line.split(":")
        card_no = int(card_info.split()[1])

        winning_numbers, my_numbers = map(str.split, numbers_str.strip().split('|'))
        winning_numbers = list(map(int, winning_numbers))
        my_numbers = list(map(int, my_numbers))

        card_dict[card_no] = {
            'winning_numbers': winning_numbers,
            'my_numbers': my_numbers,
            'instances': 1
        }
    return card_dict

def calculate_scores(cards):
    for k in cards:
        matches = len(set(cards[k]['winning_numbers']).intersection(set(cards[k]['my_numbers'])))
        score = 2 ** (matches - 1) if matches > 0 else 0
        cards[k]['score'] = score
        for i in range(1,matches+1):
            if k+1 < len(cards):
                cards[k+i]['instances'] += cards[k]['instances']
    return cards

def sum_scores(cards, score_key):
    sum = 0
    for k in cards:
        sum += cards[k][score_key]
    return sum

def main():
    with open('./2023/04input.txt') as f:
        lines = f.read().splitlines()
    cards = interpret_lines(lines)
    cards = calculate_scores(cards)
    part1 = sum_scores(cards, 'score')
    part2 = sum_scores(cards, 'instances')
    print(f"{part1 = }")
    print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
