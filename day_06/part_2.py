import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())

time = int(''.join(re.findall(r'\d', next(fc))))
dist = int(''.join(re.findall(r'\d', next(fc))))

print(len(list(filter(bool, map(lambda i: (i * (time - i)) > dist, range(time + 1))))))
