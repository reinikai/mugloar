import json
import requests
from api import Api


class Client(Api):

    params = None

    def request(self):
        json_string = requests.get(self._base_url + '/api/game').text
        self.parse(json_string)

    def parse(self, json_string):
        self.params = json.loads(json_string)
        print(self.params)

    def send_solution(self, dragon):
        print(dragon)
        print(self._base_url + '/api/game/' + str(self.params['gameId']) + '/solution')
        return requests.put(self._base_url + '/api/game/' + str(self.params['gameId']) + '/solution', json=dragon).text

