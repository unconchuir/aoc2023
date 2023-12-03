import re
from collections import defaultdict


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

gear_regex = re.compile(r'\*')
part_no_regex = re.compile(r'\d+')

gear_indices = defaultdict(lambda: [])
part_no_matches = defaultdict(lambda: [])

for line_no, line in enumerate(fc):
    for match in gear_regex.finditer(line):
        gear_indices[line_no].append(match.start())

    for match in part_no_regex.finditer(line):
        part_no_matches[line_no].append(match)

gear_ratios = []
for line_no, gear_indices in gear_indices.items():
    for gear_index in gear_indices:
        part_numbers = []
        for part_line_index in range(line_no - 1, line_no + 2):
            part_matches = part_no_matches[part_line_index]
            for part_match in part_matches:
                if part_match.start() - 1 <= gear_index <= part_match.end():
                    part_numbers.append(int(part_match.group(0)))
        if len(part_numbers) == 2:
            gear_ratios.append(part_numbers[0] * part_numbers[1])

print(sum(gear_ratios))
