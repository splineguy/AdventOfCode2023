import numpy as np
import re

def parse_input(lines,verbose=False):
    games = {}
    for line in lines:
        line = line.split(':')
        game_id = int(re.findall(r'\d+',line[0])[0])
        games[game_id] = {}

        round = 1
        results = line[-1].split(';')
        for r in results:
            games[game_id][round] = {}
            marbles = [x.strip() for x in r.split(',')]
            for marble in marbles:
                num_marble = marble.split(' ')
                games[game_id][round][num_marble[1]] = int(num_marble[0])
            if verbose:        
                print(game_id,round, games[game_id][round])
            round = round+1
    return games

def part1(games, verbose=False):
    
    bounds = {'red': 12, 'green':13, 'blue':14} 
    possible_games = []
    impossible_games = []
    for game in games:
        for round in games[game]:
            for marble in games[game][round]:
                if verbose:
                    print(game, round, marble, games[game][round][marble])
                if games[game][round][marble] > bounds[marble]:
                    impossible_games.append(game)
                    if verbose:
                        print("impossible break")
                    break
            else:
                continue
            break
        else:
            possible_games.append(game)
            continue
    result = sum(possible_games)
    print(result)

def part2(games, verbose=False):
    powers = []
    for game in games:
        bounds = {'red':0, 'green':0, 'blue':0}
        for round in games[game]:
            for marble in games[game][round]:
                if games[game][round][marble] > bounds[marble]:
                    bounds[marble] = games[game][round][marble]
        powers.append(bounds['red'] * bounds['blue'] * bounds['green'])
    print(sum(powers))

if __name__ == "__main__":

    with open('inputs/inputp2a.txt','r') as f:
        linesa = [line.strip() for line in f.readlines()]

    with open('inputs/inputp2testa.txt','r') as f:
        testa = [line.strip() for line in f.readlines()]


    games = parse_input(linesa)

    part1(games)
    part2(games)