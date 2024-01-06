#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for ele in my_string:
        if ele not in ["c","C"]:
            new_string += ele
    return new_string
