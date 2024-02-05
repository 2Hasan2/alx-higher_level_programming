#!/usr/bin/python3

"""MyList module"""


class MyList(list):
    """MyList class"""

    def __init__(self):
        """initialization"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
