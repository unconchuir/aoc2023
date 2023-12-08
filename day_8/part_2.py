import re
import math


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

directions = next(fc)
next(fc)

mapped_directions = {}
for line in fc:
    element_key, *elements = re.findall(r'[\w\d]{3}', line)
    mapped_directions[element_key] = elements

a_mapped_locations = [loc for loc in mapped_directions.keys() if loc.endswith('A')]
step_counts = []
for current_loc in a_mapped_locations:
    step_count = 0
    while not current_loc.endswith('Z'):
        for direction in directions:
            location_key = 0 if direction == "L" else 1
            current_loc = mapped_directions[current_loc][location_key]
            step_count += 1
            if current_loc.endswith('Z'):
                break
    step_counts.append(step_count)

print(math.lcm(*step_counts))
