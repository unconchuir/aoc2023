with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())


cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_values = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}


def is_five_kind(hand: str):
    return all(card == hand[0] for card in hand)


def is_four_kind(hand: str, hand_set: set):
    return len(hand_set) == 2 and any(hand.count(card) == 4 for card in hand_set)


def is_full_house(hand: str, hand_set: set):
    return len(hand_set) == 2 and any(hand.count(card) == 3 for card in hand_set)


def is_three_kind(hand: str, hand_set: set):
    return len(hand_set) == 3 and any(hand.count(card) == 3 for card in hand_set)


def is_two_pair(hand: str, hand_set: set):
    return len(hand_set) == 3 and any(hand.count(card) == 2 for card in hand_set)


def is_one_pair(hand_set: set):
    return len(hand_set) == 4


def hand_value(hand):
    return [card_values[card] for card in hand]


def rank(hand: str):
    hand_set = set(hand)
    if is_five_kind(hand):
        return 6
    elif is_four_kind(hand, hand_set):
        return 5
    elif is_full_house(hand, hand_set):
        return 4
    elif is_three_kind(hand, hand_set):
        return 3
    elif is_two_pair(hand, hand_set):
        return 2
    elif is_one_pair(hand_set):
        return 1
    else:
        return 0


hands = [line.split(' ') for line in fc]

hands.sort(key=lambda h: (rank(h[0]), hand_value(h[0])))
print(sum(int(value) * position for position, (hand, value) in enumerate(hands, 1)))
