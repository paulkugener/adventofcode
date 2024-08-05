from enum import Enum

class Hand(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

VALUES = {
    '2': "02",
    '3': "03",
    '4': "04",
    '5': "05",
    '6': "06",
    '7': "07",
    '8': "08",
    '9': "09",
    'T': "10",
    'J': "11",
    'Q': "12",
    'K': "13",
    'A': "14"
}

VALUES_P2 = {
    '2': "02",
    '3': "03",
    '4': "04",
    '5': "05",
    '6': "06",
    '7': "07",
    '8': "08",
    '9': "09",
    'T': "10",
    'J': "01",
    'Q': "12",
    'K': "13",
    'A': "14"
}

def do_(hands, part2=False):
    # xx1122334455
    d = dict()
    for hand, bid in hands:
        h = identify_poker_hand(hand, part2)
        if part2:
            d[hand] = {
            'bid': bid,
            'score': int(str(h.value) + VALUES_P2[hand[0]] + VALUES_P2[hand[1]] + VALUES_P2[hand[2]] + VALUES_P2[hand[3]] + VALUES_P2[hand[4]])
        }
        else:
            d[hand] = {
                'bid': bid,
                'score': int(str(h.value) + VALUES[hand[0]] + VALUES[hand[1]] + VALUES[hand[2]] + VALUES[hand[3]] + VALUES[hand[4]])
            }
    #print(d)
    sorted_d = dict(sorted(d.items(), key=lambda x: x[1]['score']))
    result = 0
    rank = 0
    for k, v in sorted_d.items():
        rank += 1
        result += (v['bid'] * rank)
    return result

def identify_poker_hand(hand, part2):
    card_counts = {
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'T': 0,
        'J': 0,
        'Q': 0,
        'K': 0,
        'A': 0
    }
    for card in hand:
        card_counts[card] += 1
    if part2 == False:
        if any(count == 5 for count in card_counts.values()):
            return Hand.FIVE_OF_A_KIND
        if any(count == 4 for count in card_counts.values()):
            return Hand.FOUR_OF_A_KIND
        if any(count == 3 for count in card_counts.values()) and any(count == 2 for count in card_counts.values()):
            return Hand.FULL_HOUSE
        if any(count == 3 for count in card_counts.values()):
            return Hand.THREE_OF_A_KIND
        if sum(count == 2 for count in card_counts.values()) == 2:
            return Hand.TWO_PAIR
        if any(count == 2 for count in card_counts.values()):
            return Hand.ONE_PAIR
        return Hand.HIGH_CARD
    if part2 == True:
        if any(count == 5 for count in card_counts.values()):
            return Hand.FIVE_OF_A_KIND
        if any(count + card_counts['J'] == 5 for card, count in card_counts.items() if card in '23456789TQKA'):
            return Hand.FIVE_OF_A_KIND
        
        if any(count == 4 for count in card_counts.values()):
            return Hand.FOUR_OF_A_KIND
        if any(count + card_counts['J'] == 4 for card, count in card_counts.items() if card in '23456789TQKA'):
            return Hand.FOUR_OF_A_KIND
        
        if any(count == 3 for count in card_counts.values()) and any(count == 2 for count in card_counts.values()):
            return Hand.FULL_HOUSE
        if sum(count == 2 for count in card_counts.values()) == 2 and any(count == 1 for card, count in card_counts.items() if card == 'J'):
            # two-pair and resting jack
            return Hand.FULL_HOUSE
        
        if any(count == 3 for count in card_counts.values()):
            return Hand.THREE_OF_A_KIND
        if any(count + card_counts['J'] == 3 for card, count in card_counts.items() if card in '23456789TQKA'):
            return Hand.THREE_OF_A_KIND

        if sum(count == 2 for count in card_counts.values()) == 2:
            return Hand.TWO_PAIR
        if sum(count + card_counts['J'] == 2 for card, count in card_counts.items() if card in '23456789TQKA') == 2:
            return Hand.TWO_PAIR
        
        if any(count == 2 for count in card_counts.values()):
            return Hand.ONE_PAIR
        if any(count + card_counts['J'] == 2 for card, count in card_counts.items() if card in '23456789TQKA'):
            return Hand.ONE_PAIR
        return Hand.HIGH_CARD

def main():
    with open('./2023/07input.txt') as file:
        lines = file.readlines()
    hands = [[line.split()[0], int(line.split()[1])] for line in lines]
    part1 = do_(hands)
    print(f"{part1 = }")
    part2 = do_(hands, True)
    print(f"{part2 = }")

if __name__ == '__main__':
    exit(main())
