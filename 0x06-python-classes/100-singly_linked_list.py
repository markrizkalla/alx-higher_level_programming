#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if not isinstance(next_node, Node) and next_node is not None:
            return TypeError("next_node must be a Node object")
        self.__next_node=next_node


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head == None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            temp = current.next_node
            current.next_node = new
            new.next_node = temp

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))





my_list = SinglyLinkedList()
my_list.sorted_insert(5)
my_list.sorted_insert(9)
my_list.sorted_insert(8)
my_list.sorted_insert(6)
my_list.sorted_insert(7)
print(my_list)
