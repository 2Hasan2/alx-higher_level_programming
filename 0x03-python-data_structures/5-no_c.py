#!/usr/bin/env python3
def no_c(my_string):
    new_string = "".join([ele for ele in my_string if ele.lower() != 'c'])
    return new_string

no_c("Best School")