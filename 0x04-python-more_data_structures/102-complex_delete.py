#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = {key: val for key, val in a_dictionary.items() if val != value}
    a_dictionary.clear()
    a_dictionary.update(new_dic)
    return a_dictionary
