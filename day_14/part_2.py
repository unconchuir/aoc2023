with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

all_lines = tuple(fc)


def transpose(matrix: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(map(lambda x: "".join(x), [*zip(*matrix)]))


def tilt(lines, columns: bool, reverse: bool):
    if columns:
        lines = transpose(lines)
    result = tuple("#".join("".join(sorted(chunk, reverse=reverse)) for chunk in row.split("#")) for row in lines)
    if columns:
        result = transpose(result)
    return result


def roll_north(lines):
    return tilt(lines, columns=True, reverse=True)


def roll_south(lines):
    return tilt(lines, columns=True, reverse=False)


def roll_east(lines):
    return tilt(lines, columns=False, reverse=False)


def roll_west(lines):
    return tilt(lines, columns=False, reverse=True)


def cycle(lines):
    lines = roll_north(lines)
    lines = roll_west(lines)
    lines = roll_south(lines)
    lines = roll_east(lines)
    return lines


cycle_count = 0
cache = {all_lines: 0}
max_num_iterations = 1000000000
while cycle_count < max_num_iterations:
    all_lines = cycle(all_lines)
    if all_lines in cache:
        cycle_number = cache[all_lines]
        cycle_diff = cycle_number - cycle_count
        cycle_count = max_num_iterations - (max_num_iterations % cycle_diff)
    else:
        cache[all_lines] = cycle_count
    cycle_count += 1

total = 0
num_lines = len(all_lines)
for i, line in enumerate(all_lines):
    power = num_lines - i
    total += line.count('O') * power

print(total)
