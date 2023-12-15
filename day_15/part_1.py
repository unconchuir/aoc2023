import re


with open('input.txt', 'r') as file:
    fc = file.read()

steps = list(filter(bool, re.split(r'[\n,]', fc)))


def hash_step(step: str):
    hash_value = 0
    for char in step:
        hash_value = hash_value + ord(char)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


print(sum(map(hash_step, steps)))
