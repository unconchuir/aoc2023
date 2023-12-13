with open('input.txt', 'r') as file:
    fc = file.read()

blocks = (block.split('\n') for block in fc.split('\n\n'))


def find_horizontal_reflection_point(block: list):
    for i in range(len(block) - 1):
        diff_count = 0
        for j in range(len(block)):
            if 0 <= i - j < i + 1 + j < len(block):
                for col_num in range(len(block[0])):
                    if block[i - j][col_num] != block[i + 1 + j][col_num]:
                        diff_count += 1
        if diff_count == 1:
            return i + 1


def find_vertical_reflection_point(block: list):
    for i in range(len(block[0]) - 1):
        diff_count = 0
        for j in range(len(block[0])):
            if 0 <= i - j < i + 1 + j < len(block[0]):
                for row_num in range(len(block)):
                    if block[row_num][i - j] != block[row_num][i + 1 + j]:
                        diff_count += 1
        if diff_count == 1:
            return i + 1


def parse_block(block):
    if horizontal_point := find_horizontal_reflection_point(block):
        return 100 * horizontal_point
    if vertical_point := find_vertical_reflection_point(block):
        return vertical_point


print(sum(map(parse_block, blocks)))
