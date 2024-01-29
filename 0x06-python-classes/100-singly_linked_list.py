#!/usr/bin/python3

"""Define a class Node."""

class Node:
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self, value):
		"""Set the data of the node."""
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		self.__data = value

	@property
	def next_node(self):
		return self.__next_node

	@next_node.setter
	def next_node(self, value):
		"""Set the next node of the current node."""
		if not isinstance(value, Node) and value is not None:
			raise TypeError("next_node must be a Node object")
		self.__next_node = value


class SinglyLinkedList:
	def __init__(self):
		self.__head = None

	def __str__(self):
		"""Return a string representation of the linked list."""
		nodes = []
		node = self.__head
		while node is not None:
			nodes.append(str(node.data))
			node = node.next_node
		return "\n".join(nodes)

	def sorted_insert(self, value):
		"""Insert a new node with the given value in a sorted manner."""
		new_node = Node(value)
		if self.__head is None:
			self.__head = new_node
		elif self.__head.data > value:
			new_node.next_node = self.__head
			self.__head = new_node
		else:
			node = self.__head
			while node.next_node is not None and node.next_node.data < value:
				node = node.next_node
			new_node.next_node = node.next_node
			node.next_node = new_node
