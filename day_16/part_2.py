import sys

from multiprocessing import Pool


sys.setrecursionlimit(10000000)

with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

all_lines = list(fc)
max_col = len(all_lines[0]) - 1
max_row = len(all_lines) - 1


def get_next_position(current_position, current_direction, path):
    col_no, row_no = current_position
    if not 0 <= col_no <= max_col:
        return
    if not 0 <= row_no <= max_row:
        return
    if (current_position, current_direction) in path:
        return
    path.add((current_position, current_direction))
    current_char = all_lines[row_no][col_no]

    if current_char == '.' and current_direction == 'N':
        get_next_position((col_no, row_no - 1), current_direction, path)
    if current_char == '.' and current_direction == 'S':
        get_next_position((col_no, row_no + 1), current_direction, path)
    if current_char == '.' and current_direction == 'E':
        get_next_position((col_no + 1, row_no), current_direction, path)
    if current_char == '.' and current_direction == 'W':
        get_next_position((col_no - 1, row_no), current_direction, path)
    if current_char == '|' and current_direction in 'EW':
        get_next_position((col_no, row_no - 1), 'N', path)
        get_next_position((col_no, row_no + 1), 'S', path)
    if current_char == '-' and current_direction == 'E':
        get_next_position((col_no + 1, row_no), 'E', path)
    if current_char == '-' and current_direction == 'W':
        get_next_position((col_no - 1, row_no), 'W', path)
    if current_char == '|' and current_direction == 'N':
        get_next_position((col_no, row_no - 1), 'N', path)
    if current_char == '|' and current_direction == 'S':
        get_next_position((col_no, row_no + 1), 'S', path)
    if current_char == '-' and current_direction in 'NS':
        get_next_position((col_no + 1, row_no), 'E', path)
        get_next_position((col_no - 1, row_no), 'W', path)
    if current_char == '\\' and current_direction == 'N':
        get_next_position((col_no - 1, row_no), 'W', path)
    if current_char == '\\' and current_direction == 'S':
        get_next_position((col_no + 1, row_no), 'E', path)
    if current_char == '\\' and current_direction == 'E':
        get_next_position((col_no, row_no + 1), 'S', path)
    if current_char == '\\' and current_direction == 'W':
        get_next_position((col_no, row_no - 1), 'N', path)
    if current_char == '/' and current_direction == 'N':
        get_next_position((col_no + 1, row_no), 'E', path)
    if current_char == '/' and current_direction == 'S':
        get_next_position((col_no - 1, row_no), 'W', path)
    if current_char == '/' and current_direction == 'E':
        get_next_position((col_no, row_no - 1), 'N', path)
    if current_char == '/' and current_direction == 'W':
        get_next_position((col_no, row_no + 1), 'S', path)


def get_total_from_start(start_pos, start_direction):
    path = set()
    get_next_position(start_pos, start_direction, path=path)
    return len(set(map(lambda p: p[0], path)))


start_positions = tuple()
# north
start_positions += tuple(((col, max_row), 'N') for col in range(max_col + 1))
# south
start_positions += tuple(((col, 0), 'S') for col in range(max_col + 1))
# east
start_positions += tuple(((0, row), 'E') for row in range(max_row + 1))
# west
start_positions += tuple(((max_col, row), 'W') for row in range(max_row + 1))


if __name__ == '__main__':
    totals = []
    pool = Pool()
    for position, direction in start_positions:
        pool.apply_async(get_total_from_start, (position, direction), callback=lambda v: totals.append(v))
    pool.close()
    pool.join()

    print(max(totals))
