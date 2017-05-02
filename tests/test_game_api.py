import pytest
from mugloar import game_api

@pytest.fixture
def client():
    """Returns a Client instance"""
    return game_api.Client()

def test_new_game(client):
    client.new_game()