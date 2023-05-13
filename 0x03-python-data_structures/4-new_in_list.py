#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ make a copy of a list and insert an element in a specified
    position without affect the original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
