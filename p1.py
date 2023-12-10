import numpy as np
import re


def part1(lines, verbose=False):
    sum = 0
    for line in lines:
        nums = re.findall(r'\d', line)
        val = int(nums[0])*10 + int(nums[-1])
        sum+=val
        if verbose==True:
            print(val, nums)
    print('part 1:', sum)


def part2(lines, verbose=False):
    sum = 0
    numbers = ['one','two','three','four','five','six','seven','eight','nine','1','2','3','4','5','6','7','8','9']
    values = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

    for line in lines:
        left_locs = [line.find(x) for x in numbers]
        right_locs = [line.rfind(x) for x in numbers]
        left = values[np.argmin([x if x >= 0 else np.inf for x in left_locs])]
        right = values[np.argmax(right_locs)]
        val = left*10 + right
        if val <11 or val >99:
            print('val error',val)
        sum += val
        if verbose==True:
            print(line,left,right,val)
    print('part 2:', sum)


if __name__ == "__main__":

    with open('inputs/inputp1a.txt','r') as f:
        lines = [line.strip() for line in f.readlines()]

    with open('inputs/inputp1test.txt','r') as f:
        test = [line.strip() for line in f.readlines()]
    
    part1(lines)
    part2(lines)