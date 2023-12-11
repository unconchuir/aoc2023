with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

all_lines = list(map(list, fc))

all_galaxy_co_ords = [
    (col_no, line_no)
    for line_no, line in enumerate(all_lines)
    for col_no, char in enumerate(line)
    if char != '.'
]

all_dot_row_indices = [
    line_index
    for line_index, line in enumerate(all_lines)
    if all(char == '.' for char in line)
]

all_dot_col_indices = [
    char_index
    for char_index, col_chars in enumerate(zip(*all_lines))
    if all(char == '.' for char in col_chars)
]


def num_expanses_crossed(x_co_ord_1, y_co_ord_1, x_co_ord_2, y_co_ord_2):
    num = 0
    for expanse_index in all_dot_col_indices:
        if min(x_co_ord_1, x_co_ord_2) < expanse_index < max(x_co_ord_1, x_co_ord_2):
            num += 1
    for expanse_index in all_dot_row_indices:
        if min(y_co_ord_1, y_co_ord_2) < expanse_index < max(y_co_ord_1, y_co_ord_2):
            num += 1
    return num


def get_distance(x_co_ord_1, y_co_ord_1, x_co_ord_2, y_co_ord_2):
    x_distance = abs(x_co_ord_1 - x_co_ord_2)
    y_distance = abs(y_co_ord_1 - y_co_ord_2)
    expanse = num_expanses_crossed(x_co_ord_1, y_co_ord_1, x_co_ord_2, y_co_ord_2)
    return x_distance + y_distance + expanse


total_distance = 0
while len(all_galaxy_co_ords):
    start_co_ord = all_galaxy_co_ords.pop(0)
    for co_ord in all_galaxy_co_ords:
        distance = get_distance(*start_co_ord, *co_ord)
        total_distance += distance

print(total_distance)
