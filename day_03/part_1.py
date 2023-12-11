import re
from collections import defaultdict


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

symbol_regex = re.compile(r'[^\d\.]|\*')
part_no_regex = re.compile(r'\d+')

symbol_indices = defaultdict(lambda: [])
part_no_matches = defaultdict(lambda: [])

for line_no, line in enumerate(fc):
    for match in symbol_regex.finditer(line):
        symbol_indices[line_no].append(match.start())

    for match in part_no_regex.finditer(line):
        part_no_matches[line_no].append(match)

part_nos = []
for line_no, matches in part_no_matches.items():
    for part_match in matches:
        for symbol_line_pos in range(line_no - 1, line_no + 2):
            line_symbol_indexes = symbol_indices[symbol_line_pos]
            if any(part_match.start() - 1 <= index <= part_match.end() for index in line_symbol_indexes):
                part_nos.append(int(part_match.group(0)))

print(sum(part_nos))
