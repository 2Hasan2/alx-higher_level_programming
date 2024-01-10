#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print(f"{ele}: {a_dictionary[ele]}") for ele in sorted(a_dictionary)]
