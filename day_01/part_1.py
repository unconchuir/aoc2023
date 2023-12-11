with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())


def get_numbers(line):
    digits = [c for c in line if c.isdigit()]
    return int(f'{digits[0]}{digits[-1]}')


print(sum(map(get_numbers, fc)))
