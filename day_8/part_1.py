import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

directions = next(fc)
next(fc)

mapped_directions = {}
for line in fc:
    element_key, *elements = re.findall(r'[\w\d]{3}', line)
    mapped_directions[element_key] = elements

step_count = 0
current_loc = 'AAA'
while current_loc != 'ZZZ':
    for direction in directions:
        location_key = 0 if direction == "L" else 1
        current_loc = mapped_directions[current_loc][location_key]
        step_count += 1
        if current_loc == 'ZZZ':
            break

print(step_count)
