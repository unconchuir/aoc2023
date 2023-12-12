import re
import functools


with open('input.txt', 'r') as file:
    fc = list(map(str.strip, file.readlines()))

nums_regex = re.compile(r'\d+')
conditions_regex = re.compile(r'[?#]')
next_group_regex = re.compile(r'^\.*#')
prefix_regex = re.compile(r'^\.*#+|^\.*\?')


@functools.lru_cache
def process_conditions(conditions: str, nums: tuple):
    if not nums:
        return 1 if '#' not in conditions else 0
    elif not conditions or not conditions_regex.search(conditions):
        return 0
    else:
        first_group = re.match(rf'^\.*[?#]{{{nums[0]}}}(?!#)', conditions)
        if not first_group:
            if next_group_regex.match(conditions):
                return 0
            prefix = prefix_regex.match(conditions)
            return process_conditions(conditions[len(prefix[0]):], nums)

        prefix = prefix_regex.match(conditions)
        first_group = first_group[0]

        result = process_conditions(conditions[len(first_group) + 1:], nums[1:])
        if not next_group_regex.match(conditions):
            result += process_conditions(conditions[len(prefix[0]):], nums)
        return result


def process_line(line: str):
    conditions, nums = line.strip().split()
    nums = tuple(int(x) for x in nums_regex.findall(nums)) * 5
    conditions = '?'.join(conditions for _ in range(5))
    return process_conditions(conditions, nums)


print(sum(map(process_line, fc)))
