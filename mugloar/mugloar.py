import dragon
import game
import logger
import weather

iterations = 10

game_client = game.Client()
log = logger.Logger()

# Repeat from step 1 specified amount of times
for i in range(iterations):
    # 1. Fetch new game from game API
    game_client.request()
    log.new_game(game_client.params)

    # 2. Fetch weather from "third party" weather API
    weather_client = weather.Client(game_client.params['gameId'])
    weather_client.request()

    # 3. Solves the game by selectively distributing 20 points on a dragon stats
    dragon_object = dragon.Dragon(weather_client.weather['code'])
    log.dragon(dragon_object, weather_client.weather)

    # 4. Sends the response to solve API
    result = game_client.send_solution(dragon_object.get_json())

    # 5. Logs down results somehow
    log.result(result)

log.print_stats()
