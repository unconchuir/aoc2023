import re

with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

currents = []
nexts = [int(i) for i in re.findall(r'\d+', next(fc))]

next(fc)
for line in filter(bool, fc):
    numbers = list(map(int, re.findall(r'\d+', line)))
    if not len(numbers):
        nexts.extend(currents)
        currents = nexts
        nexts = []
    else:
        current_destination, current_source, range_map = numbers
        for number in currents:
            if current_source <= number < current_source + range_map:
                distance = number - current_source
                nexts.append(current_destination + distance)
                currents = [n for n in currents if n != number]

nexts.extend(currents)
print(min(nexts))
