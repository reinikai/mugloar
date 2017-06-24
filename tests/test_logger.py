import pytest
from mugloar import dragon, logger


@pytest.fixture
def log_instance():
    """Returns a Logger instance"""
    return logger.Logger()


@pytest.fixture
def knight():
    return [('endurance', 8), ('attack', 8), ('armor', 0), ('agility', 4)]


@pytest.fixture
def dragon_instance():
    return dragon.Dragon()


@pytest.fixture
def stats_map():
    return {'attack': 'scaleThickness',
            'armor': 'clawSharpness',
            'agility': 'wingStrength',
            'endurance': 'fireBreath'}


def test_comparison(log_instance, knight, dragon_instance, stats_map):
    dragon_instance.set_relative_stats((5, 5, 5, 5), knight)
    log_instance.comparison(knight, dragon_instance, stats_map)
