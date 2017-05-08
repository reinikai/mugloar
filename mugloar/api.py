from abc import ABCMeta


class Api(metaclass=ABCMeta):

    _base_url = "http://www.dragonsofmugloar.com"

    def request(self):
        raise NotImplementedError

    def parse(self, data_string):
        raise NotImplementedError
