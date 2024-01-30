#!/usr/bin/python3
"""Defines a function that finds the biggest integer of a list."""

def max_integer(list=[]):
    """Finds the biggest integer of a list."""
    if list == []:
        return None
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max
