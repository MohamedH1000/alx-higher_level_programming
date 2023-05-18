#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    p_l = []
    for a, b in a_dictionary.items():
        if b == value:
            p_l.append(a)
    for i in p_l:
        a_dictionary.pop(i)
    return(a_dictionary)
