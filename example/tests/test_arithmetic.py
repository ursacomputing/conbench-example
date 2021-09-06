from example import arithmetic


def test_add():
    assert arithmetic.add(1, 1) == 2


def test_subtract():
    assert arithmetic.subtract(100, 1) == 99
