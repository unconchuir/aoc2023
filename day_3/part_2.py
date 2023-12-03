import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

gear_regex = re.compile(r'\*')
part_no_regex = re.compile(r'\d+')

lines = list(fc)
gear_ratios = []
for line_no, line in enumerate(lines):
    for gear_match in gear_regex.finditer(line):
        gear_index = gear_match.start()
        part_numbers = []
        for search_line_no in range(max(line_no - 1, 0), line_no + 2):
            search_line = lines[search_line_no]
            for part_match in part_no_regex.finditer(search_line):
                if part_match.start() - 1 <= gear_index <= part_match.end():
                    part_numbers.append(int(part_match.group(0)))
        if len(part_numbers) == 2:
            gear_ratios.append(part_numbers[0] * part_numbers[1])

print(sum(gear_ratios))
