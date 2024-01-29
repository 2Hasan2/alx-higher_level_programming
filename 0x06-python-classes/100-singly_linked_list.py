#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, d, n=None):
        """Initialize a new Node.

        Args:
            d (int): The data of the new Node.
            n (Node): The next node of the new Node.
        """
        self.d = d
        self.n = n

    @property
    def d(self):
        """Get/set the data of the Node."""
        return (self.__d)

    @d.setter
    def d(self, v):
        if not isinstance(v, int):
            raise TypeError("data must be an integer")
        self.__d = v

    @property
    def n(self):
        """Get/set the next_node of the Node."""
        return (self.__n)

    @n.setter
    def n(self, v):
        if not isinstance(v, Node) and v is not None:
            raise TypeError("next_node must be a Node object")
        self.__n = v


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__h = None

    def sorted_insert(self, v):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            v (Node): The new Node to insert.
        """
        new = Node(v)
        if self.__h is None:
            new.n = None
            self.__h = new
        elif self.__h.d > v:
            new.n = self.__h
            self.__h = new
        else:
            t = self.__h
            while (t.n is not None and
                    t.n.d < v):
                t = t.n
            new.n = t.n
            t.n = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        t = self.__h
        while t is not None:
            values.append(str(t.d))
            t = t.n
        return ('\n'.join(values))
