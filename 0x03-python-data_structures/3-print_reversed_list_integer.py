#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """a function that can print a list in the reverse order"""
    if my_list:
        for a in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[a]))
