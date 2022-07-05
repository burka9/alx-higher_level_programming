#!/usr/bin/python3
"""Single Linked List"""


class Node:
    """Node"""

    def __init__(self, data, next_node=None):
        """__init__"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """SinglyLinkedList"""

    def __init__(self):
        """__init__"""
        self.__head = None

    def __str__(self):
        """__str__"""
        h = self.__head
        tmp = []

        while h is not None:
            tmp.append(h.data)
            h = h.next_node

        return '\n'.join(map(str, tmp))

    def sorted_insert(self, data):
        """sorted_insert"""
        new = Node(data)

        if self.__head is None:
            self.__head = new
        elif data < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < data:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
