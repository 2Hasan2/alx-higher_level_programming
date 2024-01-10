#!/usr/bin/python3
def common_elements(set_1, set_2):
    print([ele for ele in set_1 if set_2.include(ele)])


set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

common_elements(set_1,set_2)