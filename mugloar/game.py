import json
import requests
from api import Api
from typing import Dict


class Client(Api):

    def __init__(self):
        """ Initializes instance variables. """
        self.params: Dict[str, str] = {}

    def request(self) -> None:
        json_string = requests.get(self._BASE_URL + '/api/game').text
        self.params = self.parse(json_string)

    @staticmethod
    def parse(api_response: str) -> dict:
        return json.loads(api_response)

    def send_solution(self, dragon) -> dict:
        return self.parse(requests.put(self._BASE_URL + '/api/game/' + str(self.params['gameId']) + '/solution',
                                       json=dragon).text)
