import numpy as np
import re

def parse_input(filename,verbose=False):
    with open(filename,'r') as f:
        lines = [line.strip() for line in f.readlines()]

    data = {'cards':[], 'winners':[], 'players':[]}

    for line in lines:
        card = line.split(":")
        card_number = int(re.findall(r'\d+', card[0])[0])
        numbers = card[1].split("|")
        if verbose:
            print(numbers)
        winners = [int(x) for x in re.split(r'\s+', numbers[0].strip())]
        players = [int(x) for x in re.split(r'\s+',numbers[1].strip())]
        data['cards'].append(card_number)
        data['winners'].append(winners)
        data['players'].append(players)

    return data


def part1(data, verbose=False):
    scores = []
    for i, card in enumerate(data['cards']):
        scores.append(int(2**(sum([1 if x in data['winners'][i] else 0 for x in data['players'][i]])-1)))
    result = sum(scores)
    print(result)

def part2(data, verbose=False):
    scores = []
    for i, card in enumerate(data['cards']):
        scores.append(int(sum([1 if x in data['winners'][i] else 0 for x in data['players'][i]])))
    
    nums = [1 for x in range(len(scores))]
    
    for i in range(len(nums)):
        for j in range(scores[i]):
            if j+i+1<len(nums):
                nums[j+i+1] += nums[i]
    if verbose:
        print(scores)
        print(nums)
    print(sum(nums))

if __name__ == "__main__":

    filename = 'inputs/inputp4a.txt'

    data = parse_input(filename, verbose=False)

    part1(data)
    part2(data)