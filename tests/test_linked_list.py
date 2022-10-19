"""Some special components tests."""

import pytest

from linked_list import LinkedList, Node


def test_init():
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert str(linked_list) == 'LL[]'

    linked_list = LinkedList(1, 2, 3)
    assert len(linked_list) == 3
    assert str(linked_list) == 'LL[1 > 2 > 3]'


def test_add():
    items_1 = [1, 2, 'a', 'b']
    items_2 = [True, False]
    item_3 = None

    linked_list = LinkedList()
    linked_list.add(*items_1)
    assert len(linked_list) == len(items_1)
    assert str(linked_list) == "LL[1 > 2 > 'a' > 'b']"

    linked_list.add(*items_2)
    assert len(linked_list) == len(items_1) + len(items_2)
    assert str(linked_list) == "LL[1 > 2 > 'a' > 'b' > True > False]"

    linked_list.add(item_3)
    assert len(linked_list) == len(items_1) + len(items_2) + 1
    assert str(linked_list) == "LL[1 > 2 > 'a' > 'b' > True > False > None]"


@pytest.mark.parametrize(
    ('items_1', 'items_2', 'is_equal'),
    [
        ([1, 2, '3'], [1, 2, '3'], True),
        ([1, 2, '3'], [1, 3, 2], False),
        ([1, 2, '3'], [1], False),
        ([1, 2, '3'], [], False),
    ]
)
def test_equal(items_1, items_2, is_equal):
    linked_list_1 = LinkedList(*items_1)
    linked_list_2 = LinkedList(*items_2)
    assert (linked_list_1 == linked_list_2) == is_equal


@pytest.mark.parametrize('index', (0, 1, -1, -2))
def test_index(index):
    items = [1, 2, 'a', 'b', True, False, None]
    linked_list = LinkedList(*items)
    assert linked_list[index] == Node(items[index])


def test_extra_index():
    items = [1, 2, 'a', 'b', True, False, None]
    linked_list = LinkedList(*items)
    last_index = len(linked_list) - 1
    neg_first_index = -len(linked_list)
    assert linked_list[-1] == linked_list[last_index]
    assert linked_list[0] == linked_list[neg_first_index]


def test_index_exceptions():
    items = [1, 2, 'a', 'b', True, False, None]
    linked_list = LinkedList(*items)
    with pytest.raises(IndexError):
        assert linked_list[len(items)]
    with pytest.raises(IndexError):
        assert linked_list[-len(items) - 1]


def test_type_el_by_index():
    items = [1, 2, 'a', 'b', True, False, None]
    linked_list = LinkedList(*items)
    assert isinstance(linked_list[0], Node)


@pytest.mark.parametrize(
    ('index', 'value'),
    [
        (0, 'new0'),
        (2, 'new2'),
        (-1, 'new-1'),
    ]
)
def test_set_item(index, value):
    items = [1, 2, 'a', 'b', True, False, None]
    linked_list = LinkedList(*items)
    linked_list[index] = value
    assert linked_list[index] == Node(value)


@pytest.mark.parametrize(
    ('items', 'index'),
    [
        ([0, 1, 2, 3, 4], 0),
        ([0, 1, 2, 3, 4], 1),
        ([0, 1, 2, 3, 4], -1),
    ]
)
def test_del_item(items, index):
    linked_list = LinkedList(*items)
    del linked_list[index]
    assert linked_list[index] != Node(items[index])
    assert len(linked_list) == len(items) - 1


def test_iter():
    items = [1, 2, 'a', 'b', True, False, None]
    linked_list = LinkedList(*items)
    for i, node in enumerate(linked_list):
        assert Node(items[i]) == node


def test_contains():
    items = [0, 1, 2, 3, 4]
    linked_list = LinkedList(*items)
    assert Node(0) in linked_list
    assert Node(3) in linked_list
    assert Node('0') not in linked_list


def test_reverse():
    items = [0, 1, 2, 3, 4, 5]
    linked_list = LinkedList(*items)
    for node, item in zip(
            reversed(linked_list),
            reversed(items)
    ):
        assert node.value == item
