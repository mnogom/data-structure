"""Some special components tests."""
import pytest

from pipe.utils import (
    mapf, filterf, add, power, sub, multiply,
    divide, reverse_args, cascadate, concat, push
)


def test_add():
    assert add(1)() == 1
    assert add(1)(2)() == 3
    assert add(1)(1)(1)(1)(1)() == 5


def test_power():
    assert power(2)(10)() == 1024


def test_sub():
    assert sub(5)() == 5
    assert sub(8)(3)() == 5
    assert sub(10)(1)(1)(1)(1)(1)() == 5


def test_multiply():
    assert multiply(1)() == 1
    assert multiply(5)(6)() == 30
    assert multiply(1)(2)(3)(4)(5)() == 120


def test_divide():
    assert divide(2)() == 2
    assert divide(4)(2)() == 2
    assert divide(2048)(4)(4)(4)(4)(4)() == 2


def test_reverse_args():
    assert reverse_args(divide)(4)(2)() == 0.5
    assert reverse_args(sub)(1)(4)(1)() == 2


def test_concat():
    assert concat([1])() == [1]
    assert concat([])([])() == []
    assert concat([1])([2])() == [1, 2]

    a = [1, 2, 3]
    b = [4, 5]
    c = [6, ]
    result = [1, 2, 3, 4, 5, 6]
    assert concat(a)(b)(c)() == result
    assert a != result


def test_push():
    assert push([])() is None

    a = [1, 2, 3]
    element_1 = 4
    element_2 = 5
    element_3 = 6
    result = [*a, element_1, element_2, element_3]
    push(a)(element_1)(element_2)(element_3)()
    assert a == result


def test_cascadate():
    fn_1 = cascadate(lambda x: x + 1)
    assert fn_1(2)() == 3
    fn_2 = cascadate(lambda x, y: x + y)
    assert fn_2(1)(2)() == 3
    fn_3 = cascadate(lambda *args: sum(args))
    assert fn_3(1)(2)(3)(4)(5)() == 15

    def fn_4(a, b, c, *args):
        return max(a, b, c, *args)
    assert cascadate(fn_4)(1, 2, 3)() == 3
    assert cascadate(fn_4)(1, 2, 3, 4, 5)() == 5
    with pytest.raises(TypeError) as error:
        cascadate(fn_4)(1)()
    assert 'missing' in str(error.value)


# def test_iff():
#     assert iff(True)(1)(2)() == 1
#     assert iff(False)(1)(2)() == 2


def test_mapf():
    items = [1, 2, 3]
    expected = [10, 20, 30]
    assert mapf(multiply(10))(items)() == expected

    expected = [2, 3, 4]
    add_1 = cascadate(lambda x: x + 1)
    assert mapf(add_1)(items)() == expected
    assert reverse_args(mapf)(items)(add_1)() == expected


def test_filterf():
    items = [1, 2, 3, 4]
    is_even = cascadate(lambda x: x % 2 == 0)
    expected = [2, 4]
    assert filterf(is_even)(items)() == expected
