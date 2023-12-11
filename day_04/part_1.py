# Intentionally avoiding regex in today's solutions

def parse_game_data(game_line: str) -> tuple:
    game_no_str, nums_str = game_line.split(':')
    winning_nos_str, card_nos_str = nums_str.split('|')
    game_no = int(game_no_str.split(' ')[-1])
    winning_nos = set(map(int, filter(bool, winning_nos_str.split(' '))))
    card_nos = set(map(int, filter(bool, card_nos_str.split(' '))))
    return game_no, winning_nos, card_nos


def calculate_game_points(winning_nos, card_nos):
    num_matches = len(winning_nos.intersection(card_nos))
    return pow(2, num_matches - 1) if num_matches else 0


def process_games(line):
    game_no, winning_nos, card_nos = parse_game_data(line)
    return calculate_game_points(winning_nos, card_nos)


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

print(sum(map(process_games, fc)))
