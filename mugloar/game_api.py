import json
import requests


class Client:

    def new_game(self):
        game_body = requests.get('http://www.dragonsofmugloar.com/api/game').text
        return json.loads(game_body)



class Parser:

