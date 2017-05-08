import requests
import defusedxml.ElementTree as ElemTree
from api import Api


class Client(Api):

    """Cheat sheet
       NMR = normal weather = normal fights
       FUNDEFINEDG = fog
       HVA = rain
       SRO = storm
       T E = dry
    """

    game_id = None
    weather = {}

    def __init__(self, game_id):
        if game_id < 1:
            raise RuntimeError("Invalid game ID")
        self.game_id = game_id

    def request(self):
        game_body = requests.get(self._base_url + '/weather/api/report/' + str(self.game_id)).text
        self.parse(game_body)

    def parse(self, xml_string):
        root = ElemTree.fromstring(xml_string)
        self.weather = convert_to_dict(root)


def convert_to_dict(xml_element):
    dictionary = {}
    for child in xml_element:
        dictionary[child.tag] = child.text
    return dictionary
