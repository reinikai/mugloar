#!/usr/bin/env python3

import dragon
import game
import logger
import weather

import itertools
import time

# Specify number of knights to battle.
BATTLE_COUNT = 30

USE_SOLVER = True

game_client = game.Client()
log = logger.Logger()
dragon_object = dragon.Dragon()

def dispatch_dragon(dragon_stats, knight, relative=False):
    """ Helper function for sending off a dragon to battle """

    global dragon_number
    dragon_number += 1

    if relative:
        dragon_object.set_relative_stats(dragon_stats, knight)
    else:
        dragon_object.set_stats(*dragon_stats)

    log.dragon(dragon_object, dragon_number)

    # 4. Sends the response to solve API
    battle_result = game_client.send_solution(dragon_object.get_json())

    # 5. Logs down results somehow
    log.result(battle_result)

    if battle_result['status'] == "Victory":
        # Output comparison of knight's and dragon's stats to ease
        # development of new solution algorithms.
        log.comparison(knight, dragon_object, dragon.STATS_MAP)

    return battle_result


for battle_number in range(BATTLE_COUNT):
    """ Repeat from step 1 specified amount of times, a.k.a main loop """

    # Keep track of how many dragon's we've used in each battle.
    dragon_number = 0

    # 1. Fetch new game from game API
    game_client.request()
    log.new_game(game_client.params)

    # 2. Fetch weather from "third party" weather API
    weather_client = weather.Client(game_client.params['gameId'])
    weather_client.request()
    log.weather(weather_client.weather)

    # Remove knight's name (string) so that sorting of integers works as expected.
    knight_stats = game_client.params['knight']
    del knight_stats['name']
    # Sort opponent's stats from high to low so that we can match points.
    knight_stats = sorted(knight_stats.items(), key=lambda x: x[1], reverse=True)

    # 3. Solves the game by selectively distributing 20 points on a dragon's stats
    if weather_client.weather['code'] == 'T E':
        # Draught requires a 'balanced' dragon.
        result = dispatch_dragon((5, 5, 5, 5), knight_stats)
    elif weather_client.weather['code'] == 'FUNDEFINEDG':
        # Fog means we're unseen, no need to fly.
        result = dispatch_dragon((8, 8, 0, 4), knight_stats)
    elif weather_client.weather['code'] == 'SRO':
        # Doesn't really matter what we do in a storm - EVERYONE DIES!
        result = dispatch_dragon((10, 10, 0, 0), knight_stats)
    elif weather_client.weather['code'] == 'NMR':
        # Normal weather, we can calculate a solution relative to the knight's stats.
        # This seems to be the typical case, which offers a ~80% battle success ratio.
        result = dispatch_dragon((+2, 0, -1, -1), knight_stats, True)

        # For the remaining ~20%.
        if result['status'] != "Victory":
            result = dispatch_dragon((-1, +2, -1, 0), knight_stats, True)
        if result['status'] != "Victory":
            result = dispatch_dragon((+2, -1, -1, 0), knight_stats, True)
    else:
        # Fire is useless in the rain.
        # Additional claw-sharpening is needed to destroy the umbrellaboats.
        result = dispatch_dragon((5, 10, 5, 0), knight_stats)

    # We didn't win the battle using the predefined (hard-coded) solutions :(
    # Invoke a loop that goes through all possible solutions for this battle.
    if USE_SOLVER and weather_client.weather['code'] != "SRO" and result['status'] != "Victory":
        possible_solutions = dragon.possible_solutions()
        for solution in possible_solutions:
            # This is kind of API-intensive, so invoke a small delay between iterations.
            time.sleep(1)

            # Generate distinct compositions of partitions.
            permutations = set(itertools.permutations(solution))

            for permutation in permutations:
                result = dispatch_dragon(*permutation, knight_stats)

                if result['status'] == "Victory":
                    # No need to try the rest of the solutions if we've won :)
                    break
            else:
                continue  # executed if the inner loop ended normally (no break)
            break  # executed if 'continue' was skipped (break)

    # Keep track of what this battle's final outcome was.
    log.battle(result['status'])

# Output a summary of all battles we've fought today.
log.print_stats()
