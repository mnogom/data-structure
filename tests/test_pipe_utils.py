"""Some special components tests."""

from pipe.utils import (
    partial_fn, iff, mapf, filterf, add, power, sub, multiply, divide, reverse_args
)


def test_add():
    assert add(1)(2) == 3


def test_power():
    assert power(2)(10) == 1024


def test_sub():
    assert sub(8)(3) == 5


def test_multiply():
    assert multiply(5)(6) == 30


def test_divide():
    assert divide(4)(2) == 2


def test_reverse_args():
    assert reverse_args(divide)(4)(2) == 0.5


def test_partial_fn():
    def sum(a, b):
        return a + b
    add_5 = partial_fn(sum)(5)
    assert add_5(15) == 20


def test_iff():
    assert iff(True)(1)(2) == 1
    assert iff(False)(1)(2) == 2


def test_mapf():
    items = [1, 2, 3]
    expected = [10, 20, 30]
    assert mapf(multiply(10))(items) == expected


def test_filterf():
    items = [1, 2, 3, 4]
    is_even = lambda x: x % 2 == 0
    expected = [2, 4]
    assert filterf(is_even)(items) == expected
