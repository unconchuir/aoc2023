with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())


def get_next_value(line_nums):
    if len(set(line_nums)) == 1:
        return line_nums[0]
    next_number = get_next_value([b - a for a, b in zip(line_nums, line_nums[1:])])
    return line_nums[-1] + next_number


print(sum(get_next_value(list(map(int, line.split(' ')))) for line in fc))
