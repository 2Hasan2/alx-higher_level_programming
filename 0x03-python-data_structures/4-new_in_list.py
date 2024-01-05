#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx > length - 1 or idx < 0):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
