# what the opponent plays
# A rock
# B paper
# C scissors

# what you play
# X rock
# Y paper
# Z scissors

D = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

OUTCOME = {
    'X': 'lost',
    'Y': 'draw',
    'Z': 'won'
}

SCORE = {
    'lost': 0,
    'draw': 3,
    'won': 6
}

def compute_shape_score(shape):
    match shape:
        case 'rock':
            return 1
        case 'paper':
            return 2
        case 'scissors':
            return 3
    return 0

def compute_outcome_score(round):
    result = ''
    opp = D[round[0]]
    me = D[round[1]]
    if opp == me:
        result = 'draw'
    elif opp == 'rock':
        if me == 'scissors':
            result = 'lost'
        elif me == 'paper':
            result = 'won'
    elif opp == 'scissors':
        if me == 'paper':
            result = 'lost'
        elif me == 'rock':
            result = 'won'
    elif opp == 'paper':
        if me == 'scissors':
            result = 'won'
        elif me == 'rock':
            result = 'lost'
    return SCORE[result]

def compute_pick(round):
    pick = ''
    outcome = OUTCOME[round[1]]
    opp = D[round[0]]
    match outcome:
        case 'lost':
            match opp:
                case 'rock':
                    pick = 'scissors'
                case 'paper':
                    pick = 'rock'
                case 'scissors':
                    pick = 'paper'
        case 'won':
            match opp:
                case 'rock':
                    pick = 'paper'
                case 'paper':
                    pick = 'scissors'
                case 'scissors':
                    pick = 'rock'
        case 'draw':
            pick = opp
    return pick

with open('2022/02input') as file:
    a = [line.strip().split(' ') for line in file]
    part1_score = 0
    part2_score = 0
    for round in a:
        part1_score += compute_shape_score(D[round[1]])
        part1_score += compute_outcome_score(round)
        part2_pick = compute_pick(round)
        part2_score += compute_shape_score(part2_pick)
        part2_score += SCORE[OUTCOME[round[1]]]
    print('part1: {}'.format(part1_score))
    print('part2: {}'.format(part2_score))
