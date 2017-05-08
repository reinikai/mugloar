import json
import requests
from api import Api


class Client(Api):

    params = None

    def request(self):
        json_string = requests.get(self._base_url + '/api/game').text
        self.params = self.parse(json_string)

    def parse(self, json_string):
        return json.loads(json_string)

    def send_solution(self, dragon):
        return self.parse(requests.put(self._base_url + '/api/game/' + str(self.params['gameId']) + '/solution', json=dragon).text)
