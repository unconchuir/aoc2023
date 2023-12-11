import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

num_regexes = {
    1: re.compile(r'one|1'),
    2: re.compile(r'two|2'),
    3: re.compile(r'three|3'),
    4: re.compile(r'four|4'),
    5: re.compile(r'five|5'),
    6: re.compile(r'six|6'),
    7: re.compile(r'seven|7'),
    8: re.compile(r'eight|8'),
    9: re.compile(r'nine|9'),
}


def get_numbers(line: str) -> int:
    all_matches = {
        index: num
        for num, regex in num_regexes.items()
        for index in (m.start() for m in regex.finditer(line))
    }
    lower_index = min(all_matches.keys())
    upper_index = max(all_matches.keys())
    return (all_matches[lower_index] * 10) + all_matches[upper_index]


print(sum(get_numbers(file_line) for file_line in fc))
