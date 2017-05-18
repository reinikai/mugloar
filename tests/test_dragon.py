import pytest
from mugloar import dragon


def test_partition():
    for solution in dragon.partition(20, 4, 0, 10):
        print(solution)
        assert abs(solution[0]) + abs(solution[1]) + abs(solution[2]) + abs(solution[3]) == 20
