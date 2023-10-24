#!/usr/bin/python3

"""The Node and SinglyLinkedList classes."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new node.

        Args:
            data (int): The data value for the node.
            next_node (Node, optional): Reference
            to the next node in the list. Defaults to None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Get or set the data value of the node."""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get or set the reference to the next node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct
        sorted position in the list (increasing order).

        Args:
            value (int): The data value to be inserted into the list.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur.next_node is not None and cur.next_node.data < value:
                cur = cur.next_node
            new_node.next_node = cur.next_node
            cur.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            str: A string representation of the list
            with one node number per line.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
