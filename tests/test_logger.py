import pytest
from mugloar import dragon, logger

@pytest.fixture
def log_instance():
    """Returns a Logger instance"""
    return logger.Logger()

@pytest.fixture
def knight():
    return {'agility': 8, 'endurance': 8, 'name': 'Sir. Stephen Mathis of Nova Scotia', 'armor': 0, 'attack': 4}

@pytest.fixture
def dragon_instance(knight):
    return dragon.Dragon('NMR', knight)

@pytest.fixture
def stats_map():
    return {'attack': 'scaleThickness',
            'armor': 'clawSharpness',
            'agility': 'wingStrength',
            'endurance': 'fireBreath'}

def test_comparison(log_instance, knight, dragon_instance, stats_map):
    log_instance.comparison(knight, dragon_instance, stats_map)
