import pytest
from mugloar import dragon


@pytest.fixture
def dragon_instance():
    return dragon.Dragon()


@pytest.fixture
def knight():
    return [('endurance', 8), ('attack', 5), ('armor', 4), ('agility', 3)]


@pytest.fixture
def dragon_stats():
    return 10, 10, 0, 0


def test_set_relative_stats(dragon_instance, dragon_stats, knight):
    dragon_instance.set_relative_stats(dragon_stats, knight)
    assert dragon_instance.dragon_stats['scaleThickness'] == 2
    assert dragon_instance.dragon_stats['clawSharpness'] == 0
    assert dragon_instance.dragon_stats['wingStrength'] == 0
    assert dragon_instance.dragon_stats['fireBreath'] == 18


def test_set_stats(dragon_instance, dragon_stats):
    dragon_instance.set_stats(*dragon_stats)
    assert dragon_instance.dragon_stats['scaleThickness'] == 10
    assert dragon_instance.dragon_stats['clawSharpness'] == 10
    assert dragon_instance.dragon_stats['wingStrength'] == 0
    assert dragon_instance.dragon_stats['fireBreath'] == 0


def test_get_json(dragon_instance, dragon_stats):
    dragon_instance.set_stats(*dragon_stats)
    assert dragon_instance.get_json() == {'dragon': {'scaleThickness': 10,
                                                     'clawSharpness': 10,
                                                     'wingStrength': 0,
                                                     'fireBreath': 0}}


def test_partition():
    for solution in dragon.partition(20, 4, 0, 10):
        assert abs(solution[0]) + abs(solution[1]) + abs(solution[2]) + abs(solution[3]) == 20
