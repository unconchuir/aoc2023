import re


with open('input.txt', 'r') as file:
    fc = file.read()

steps = list(filter(bool, re.split(r'[\n,]', fc)))
boxes = {}


def hash_label(label: str):
    hash_value = 0
    for char in label:
        hash_value = ((hash_value + ord(char)) * 17) % 256
    return hash_value


def process_step(step: str):
    if '=' in step:
        label, focal_length = step.split('=')
        box_num = hash_label(label)
        boxes[box_num] = boxes.get(box_num, [])
        for i, (l, fl) in enumerate(boxes[box_num]):
            if l == label:
                del boxes[box_num][i]
                boxes[box_num].insert(i, (label, int(focal_length)))
                return
        boxes[box_num].append((label, int(focal_length)))
    else:
        label, *_ = step.split('-')
        for box, lenses in boxes.items():
            for i, lens in enumerate(lenses):
                if lens[0] == label:
                    del boxes[box][i]


def compute_total():
    total = 0
    for box_num, lenses in boxes.items():
        for i, (label, focal_length) in enumerate(lenses, 1):
            total += (box_num + 1) * i * focal_length
    return total


for step_str in steps:
    process_step(step_str)
print(compute_total())
