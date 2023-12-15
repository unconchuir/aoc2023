import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

all_lines = list(fc)
group_regex = re.compile(r'[O\.]*#*')


def sorter(char: str):
    if char == 'O':
        return 0
    elif char == '.':
        return 1
    else:
        return 2


def roll_north(lines):
    columns = list(map(lambda c: ''.join(c), zip(*lines)))

    for i, col in enumerate(columns):
        new_col = ''
        for match in group_regex.finditer(col):
            if match.group():
                num_o = match.group().count('O')
                num_dot = match.group().count('.')
                num_hash = match.group().count('#')
                new_col += 'O' * num_o + '.' * num_dot + '#' * num_hash
        columns[i] = new_col
    return list(map(lambda c: ''.join(c), zip(*columns)))


total = 0
all_lines = roll_north(all_lines)
num_lines = len(all_lines)
for i, line in enumerate(all_lines):
    print(line)
    power = num_lines - i
    total += line.count('O') * power

print(total)
