#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if (idx > length - 1 or idx < 0):
        return None
    return my_list[idx]
