from typing import Union


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __eq__(self, target):
        if isinstance(target, Node):
            return self.value == target.value
        raise TypeError('Can compare only nodes')

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self, *items):
        self.__length = 0
        self.__head = None
        if items:
            self.add(*items)

    def __repr__(self):
        output = ''
        current_node = self.__head
        while current_node:
            if output:
                output = f'{output} > {current_node.value.__repr__()}'
            else:
                output = f'{current_node.value.__repr__()}'
            current_node = current_node.next
        return f'LL[{output}]'

    def __len__(self):
        return self.__length

    def __eq__(self, target):
        if not (isinstance(target, LinkedList)):
            raise TypeError('Can compare only LinkedList')
        if len(self) != len(target):
            return False
        current_node_1 = self.__head
        current_node_2 = target.__head
        while current_node_1.next:
            if current_node_1 != current_node_2:
                return False
            current_node_1 = current_node_1.next
            current_node_2 = current_node_2.next
        return True

    def __getitem__(self, item: Union[int, slice]):
        if item > 0 and item >= len(self):
            raise IndexError('Index is out of range')
        if item < 0 and abs(item) > len(self):
            raise IndexError('Index is out of range')
        if item < 0:
            item = len(self) + item
        current_node = self.__head
        for i in range(item):
            current_node = current_node.next
        return current_node

    def __contains__(self, item):
        for node in self:
            if node == item:
                return True
        return False

    def __setitem__(self, index, value):
        self[index].value = value

    def __delitem__(self, index):
        if index == 0:
            self.__head = self.__head.next
        else:
            self[index - 1].next = self[index + 1]
        self.__length -= 1

    def __iter__(self):
        dummy_head = Node()
        dummy_head.next = self.__head
        self.current_node = dummy_head
        return self

    def __next__(self):
        if self.current_node.next:
            self.current_node = self.current_node.next
            return self.current_node
        raise StopIteration

    def __reversed__(self):
        reversed_linked_list = LinkedList()
        for i in range(1, len(self) + 1):
            reversed_linked_list.add(self[-i].value)
        return reversed_linked_list

    def add(self, *values):
        dummy_head = Node()
        current_node = dummy_head
        for value in values:
            current_node.next = Node(value)
            current_node = current_node.next
            self.__length += 1
        if not self.__head:
            self.__head = dummy_head.next
        else:
            iter_node = self.__head
            while iter_node.next:
                iter_node = iter_node.next
            iter_node.next = dummy_head.next
