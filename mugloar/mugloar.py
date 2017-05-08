import dragon
import game
import weather

iterations = 1
wins = 0

game_client = game.Client()

# Repeat from step 1 specified amount of times
for i in range(iterations):
    # 1. Fetch new game from game API
    game_client.request()

    # 2. Fetch weather from "third party" weather API
    weather_client = weather.Client(game_client.params['gameId'])
    weather_client.request()

    # 3. Solves the game by selectively distributing 20 points on a dragon stats
    dragon = dragon.Dragon(weather_client.weather['code'])

    # 4. Sends the response to solve API
    result = game_client.send_solution(dragon.get_json())

    # 5. Logs down results somehow
    print(result)

print('Success rate: ' + str(wins/iterations))
