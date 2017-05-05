import requests
import xml.etree.ElementTree as ET


class Client:

    game_id = None

    def __init__(self, game_id):
        if game_id < 1:
            raise RuntimeError("Invalid game ID")
        self.game_id = game_id

    def get_weather(self):
        game_body = requests.get('http://www.dragonsofmugloar.com/weather/api/report/' + self.game_id).text
        return json.loads(game_body)


class Parser:

    def __init__(self, xml_string):
        root = ET.fromstring(xml_string)
