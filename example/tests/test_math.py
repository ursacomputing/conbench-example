from example import math


def test_add():
    assert math.add(1, 1) == 2


def test_subtract():
    assert math.subtract(100, 1) == 99
