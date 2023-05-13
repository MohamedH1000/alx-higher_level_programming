#!/usr/bin/python3
def no_c(my_string):
    output = my_string.translate({ord(a): None for a in 'cC'})
    return output
