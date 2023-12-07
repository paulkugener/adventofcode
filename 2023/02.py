import sys

def interpret_lines(lines):
    games = {}
    for line in lines:
        game, sets = line.strip().split(':')
        _, id_ = game.strip().split(' ')
        set_list = sets.strip().split(';')
        games[id_] = interpret_sets(set_list)
    return games

def interpret_sets(set_list):
    all_sets = []
    for s in set_list:
        d = {'red': 0, 'green': 0, 'blue': 0}
        ss = s.strip().split(',')
        for c in ss:
            amount, color = c.strip().split(' ')
            d[color] = d[color] + int(amount)
        all_sets.append(d)
    return all_sets

def sum_valid_games_ids(games, r, g, b):
    sum = 0
    for game_id, game_sets in games.items():
        if is_game_possible(game_sets, r, g, b):
            sum = sum + int(game_id)
    return sum

def is_game_possible(game, r, g, b):
    for set in game:
        if set['red'] > r or set['green'] > g or set['blue'] > b:
            return False
    return True

def sum_power_of_sets(games):
    sum = 0
    for game in games.values():
        d = {'red': 0, 'green': 0, 'blue': 0}
        for s in game:
            for color in ['red', 'green', 'blue']:
                if s[color] > d[color]:
                    d[color] = s[color]
        power = d['red'] * d['green'] * d['blue']
        sum = sum + power
    return sum

def main():
    with open('./2023/02input.txt') as f:
        lines = f.read().splitlines()
    games = interpret_lines(lines)
    part1 = sum_valid_games_ids(games, 12, 13, 14)
    part2 = sum_power_of_sets(games)
    print(f"{part1 = }")
    print(f"{part2 = }")

if __name__ == '__main__':
    sys.exit(main())
