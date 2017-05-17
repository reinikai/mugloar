#!/usr/bin/env python3

import dragon
import game
import logger
import weather

import itertools
import time

# Specify number of knights to battle.
BATTLE_COUNT = 30

game_client = game.Client()
log = logger.Logger()

# Repeat from step 1 specified amount of times
for i in range(BATTLE_COUNT):
    # 1. Fetch new game from game API
    game_client.request()
    log.new_game(game_client.params)

    # 2. Fetch weather from "third party" weather API
    weather_client = weather.Client(game_client.params['gameId'])
    weather_client.request()
    log.weather(weather_client.weather)

    # 3. Solves the game by selectively distributing 20 points on a dragon stats
    dragon_object = dragon.Dragon(weather_client.weather['code'], game_client.params['knight'])
    log.dragon(dragon_object)

    # 4. Sends the response to solve API
    result = game_client.send_solution(dragon_object.get_json())

    # 5. Logs down results somehow
    log.result(result)

    # We didn't win the battle using the predefined (hard-coded) solutions :(
    # Invoke a loop that goes through all possible solutions for this battle.
    if weather_client.weather['code'] != "SRO" and result['status'] != "Victory":
        i = 1 # First dragon was already sent and it lost, remember?

        possible_solutions = dragon.possible_solutions()
        for solution in possible_solutions:
            # This is kind of API-intensive, so invoke a small delay between iterations.
            time.sleep(1)

            # Generate distinct compositions of partitions.
            permutations = set(itertools.permutations(solution))

            for permutation in permutations:
                i += 1
                dragon_object.set_stats(*permutation)
                log.dragon(dragon_object, i)
                result = game_client.send_solution(dragon_object.get_json())
                log.result(result)

                if result['status'] == "Victory":
                    break
            else:
                continue  # executed if the inner loop ended normally (no break)
            break  # executed if 'continue' was skipped (break)

    # Keep track of what this battle's final outcome was.
    log.battle(result['status'])

# Output a summary of all battles we've fought today.
log.print_stats()