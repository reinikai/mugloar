import requests
import defusedxml.ElementTree as ElemTree
from api import Api
from typing import Dict


class Client(Api):

    def __init__(self, game_id: int):
        """ Initializes instance variables. """
        if game_id < 1:
            raise RuntimeError("Invalid game ID")
        self.game_id = game_id
        self.weather: Dict[str, str] = {}

    def request(self) -> None:
        game_body = requests.get(self._BASE_URL + '/weather/api/report/' + str(self.game_id)).text
        self.parse(game_body)

    def parse(self, xml: str) -> None:
        root = ElemTree.fromstring(xml)
        self.weather = convert_to_dict(root)


def convert_to_dict(xml_element) -> dict:
    dictionary = {}
    for child in xml_element:
        dictionary[child.tag] = child.text
    return dictionary
