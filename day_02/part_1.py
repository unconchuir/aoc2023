import re


with open('input.txt', 'r') as file:
    fc = map(str.strip, file.readlines())


def process_game_string(line) -> int:
    game_id = re.search(r'(?:Game )(\d+)', line).group(1)

    if any(int(m.group(1)) > 12 for m in re.finditer(r'(\d+)(?: red)', line)):
        return 0
    if any(int(m.group(1)) > 13 for m in re.finditer(r'(\d+)(?: green)', line)):
        return 0
    if any(int(m.group(1)) > 14 for m in re.finditer(r'(\d+)(?: blue)', line)):
        return 0

    return int(game_id)


print(sum(map(process_game_string, fc)))
