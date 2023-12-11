# Intentionally avoiding regex in today's solutions
# This solution could probably do with some cleanup
def parse_game_data(game_line: str) -> tuple:
    """
    Parse a game line in to a tuple of game number, winning numbers and game numbers
    """
    game_no_str, nums_str = game_line.split(':')
    winning_nos_str, card_nos_str = nums_str.split('|')
    game_no = int(game_no_str.split(' ')[-1])
    winning_nos = set(map(int, filter(bool, winning_nos_str.split(' '))))
    card_nos = set(map(int, filter(bool, card_nos_str.split(' '))))
    return game_no, winning_nos, card_nos


def get_all_cards(game_lines) -> dict:
    """
    Produce a dict where the key is the game number and the value is a tuple of winning number and game numbers
    """
    cards = {}
    for line in game_lines:
        game_no, winning_nos, card_nos = parse_game_data(line)
        cards[game_no] = (winning_nos, card_nos)
    return cards


def process_all_games(game_lines) -> dict:
    """
    Produce a dict of the number of all games, where the key is the game number and the value is the number of copies
    """
    cards = get_all_cards(game_lines)
    upper_card_limit = max(cards.keys())
    cards_owned = {i: 1 for i in range(upper_card_limit + 1)}
    for game_no, (winning_nos, card_nos) in cards.items():
        num_matches = len(winning_nos.intersection(card_nos))
        if not num_matches:
            continue
        for i in range(game_no + 1, game_no + num_matches + 1):
            cards_owned[min(i, upper_card_limit)] += cards_owned[game_no]
    return cards_owned


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

print(sum(process_all_games(fc).values()))
