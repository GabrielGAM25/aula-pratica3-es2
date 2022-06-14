from fibonacci import fibonacci


def test_negative():
    assert fibonacci(-1) == 0


def test_zero():
    assert fibonacci(0) == 0


def test_one():
    assert fibonacci(1) == 1


def test_large():
    assert fibonacci(11) == 89
