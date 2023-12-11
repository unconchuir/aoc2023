import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())


def process_game_string(line: str) -> int:
    reds = max(int(m.group(1)) for m in re.finditer(r'(\d+)(?: red)', line))
    greens = max(int(m.group(1)) for m in re.finditer(r'(\d+)(?: green)', line))
    blues = max(int(m.group(1)) for m in re.finditer(r'(\d+)(?: blue)', line))
    return reds * greens * blues


print(sum(map(process_game_string, fc)))
