import re

from functools import reduce


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

times = map(int, re.findall(r'\d+', next(fc)))
distances = map(int, re.findall(r'\d+', next(fc)))

wins = (
    len(list(filter(bool, map(lambda i: (i * (time - i)) > distance, range(time + 1)))))
    for time, distance in zip(times, distances)
)

print(reduce(int.__mul__, wins))
