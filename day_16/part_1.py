import sys


sys. setrecursionlimit(10000000)

with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

all_lines = list(fc)


max_col = len(all_lines[0]) - 1
max_row = len(all_lines) - 1
path = set()


def get_next_position(current_position, current_direction):
    col_no, row_no = current_position
    if not 0 <= col_no <= max_col:
        return
    if not 0 <= row_no <= max_row:
        return
    if (current_position, current_direction) in path:
        return
    path.add((current_position, current_direction))
    current_char = all_lines[row_no][col_no]
    # TODO: Cleanup, this can be reduced to finding the direction using chars and working form the new direction
    if current_char == '.' and current_direction == 'N':
        get_next_position((col_no, row_no - 1), current_direction)
    elif current_char == '.' and current_direction == 'S':
        get_next_position((col_no, row_no + 1), current_direction)
    elif current_char == '.' and current_direction == 'E':
        get_next_position((col_no + 1, row_no), current_direction)
    elif current_char == '.' and current_direction == 'W':
        get_next_position((col_no - 1, row_no), current_direction)
    elif current_char == '|' and current_direction in 'EW':
        get_next_position((col_no, row_no - 1), 'N')
        get_next_position((col_no, row_no + 1), 'S')
    elif current_char == '-' and current_direction == 'E':
        get_next_position((col_no + 1, row_no), 'E')
    elif current_char == '-' and current_direction == 'W':
        get_next_position((col_no - 1, row_no), 'W')
    elif current_char == '|' and current_direction == 'N':
        get_next_position((col_no, row_no - 1), 'N')
    elif current_char == '|' and current_direction == 'S':
        get_next_position((col_no, row_no + 1), 'S')
    elif current_char == '-' and current_direction in 'NS':
        get_next_position((col_no + 1, row_no), 'E')
        get_next_position((col_no - 1, row_no), 'W')
    elif current_char == '\\' and current_direction == 'N':
        get_next_position((col_no - 1, row_no), 'W')
    elif current_char == '\\' and current_direction == 'S':
        get_next_position((col_no + 1, row_no), 'E')
    elif current_char == '\\' and current_direction == 'E':
        get_next_position((col_no, row_no + 1), 'S')
    elif current_char == '\\' and current_direction == 'W':
        get_next_position((col_no, row_no - 1), 'N')
    elif current_char == '/' and current_direction == 'N':
        get_next_position((col_no + 1, row_no), 'E')
    elif current_char == '/' and current_direction == 'S':
        get_next_position((col_no - 1, row_no), 'W')
    elif current_char == '/' and current_direction == 'E':
        get_next_position((col_no, row_no - 1), 'N')
    elif current_char == '/' and current_direction == 'W':
        get_next_position((col_no, row_no + 1), 'S')


get_next_position((0, 0), 'E')
print(len(set(map(lambda p: p[0], path))))

