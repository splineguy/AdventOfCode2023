import numpy as np
import re

def parse_input(filename,verbose=False):
    with open(filename,'r') as f:
        data = [line.strip() for line in f.readlines()]

    digit_search = re.compile(r'\d+')
    part_search = re.compile(r'[^0-9\.]')

    nums = []
    parts = []
    
    for i, d in enumerate(data):
        digits = digit_search.finditer(d)
        for digit in digits:
            start, end = digit.span()
            num = int(digit.group())
            nums.append([num, i, start, end])
        
        ps = part_search.finditer(d)
        for p in ps:
            start, end = p.span()
            part = p.group()
            parts.append([part, i, start])

    if verbose:
        for num in nums:
            print(num)
        for part in parts:
            print(part)

    return nums, parts


def part1(nums, parts, verbose=False):
    part_numbers = []
    for part in parts:
        for num in nums:
            if abs(num[1] - part[1]) < 2:
                if part[2] >= (num[2] - 1) and part[2] <= num[3]:
                    part_numbers.append(num[0])
    print(sum(part_numbers))

def part2(games, verbose=False):
    gear_ratios = []
    for part in parts:
        gears = []
        if part[0] == '*':
            for num in nums:
                if abs(num[1] - part[1]) < 2:
                    if part[2] >= (num[2] - 1) and part[2] <= num[3]:
                        gears.append(num[0])
            if len(gears)==2:
                gear_ratios.append(gears[0]*gears[1])
    print(sum(gear_ratios))

if __name__ == "__main__":

    filename = 'inputs/inputp3a.txt'

    nums, parts = parse_input(filename, verbose=False)

    part1(nums, parts)
    part2(nums, parts)