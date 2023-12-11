import re
from functools import reduce

with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

currents = []
nexts = list(map(int, re.findall(r'\d+', next(fc))))
unmapped = []

next(fc)
for line in filter(bool, fc):
    numbers = re.findall(r'\d+', line)
    if len(numbers) == 0:
        currents = nexts
        currents.extend(unmapped)
        nexts = []
        unmapped = []
    else:
        currents.extend(unmapped)
        unmapped = []
        numbers = map(int, numbers)
        current_destination, current_source, range_map = numbers

        while len(currents) > 0:
            if currents[0] - range_map < current_source < currents[0] + currents[1]:
                to_map_start = max(currents[0], current_source)
                to_map_end = min(current_source + range_map, currents[0] + currents[1])
                to_map_range = to_map_end - to_map_start

                mapped_start = current_destination + to_map_start - current_source
                nexts.extend([mapped_start, to_map_range])

                if currents[0] < to_map_start:
                    left_start = currents[0]
                    left_end = current_source
                    left_range = current_source - currents[0]
                    currents.extend((left_start, left_range))

                if currents[0] + currents[1] > to_map_end:
                    right_start = current_source + range_map
                    right_end = currents[0] + currents[1]
                    right_range = right_end - right_start
                    currents.extend((right_start, right_range))
            else:
                unmapped.extend(currents[0:2])

            currents = currents[2:]

currents = nexts
currents.extend(unmapped)

print(reduce(min, currents[::2]))
