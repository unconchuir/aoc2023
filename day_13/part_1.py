with open('input.txt', 'r') as file:
    fc = file.read()

blocks = (block.split('\n') for block in fc.split('\n\n'))


def find_horizontal_reflection_point(block: list):
    if len(set(block)) == len(block):
        return  # No horizontal reflection
    for i in range(len(block) - 1):
        if block[i] == block[i + 1]:
            if all(a == b for a, b in zip(block[i::-1], block[i + 1:])):
                return i + 1


def find_vertical_reflection_point(block: list):
    columns = list(zip(*block))
    for i in range(len(columns) - 1):
        if columns[i] == columns[i + 1]:
            if all(a == b for a, b in zip(columns[i::-1], columns[i + 1:])):
                return i + 1


def parse_block(block):
    if horizontal_point := find_horizontal_reflection_point(block):
        return 100 * horizontal_point
    if vertical_point := find_vertical_reflection_point(block):
        return vertical_point


print(sum(map(parse_block, blocks)))

