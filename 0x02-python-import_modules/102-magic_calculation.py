#!/usr/bin/python3
from magic_calculation_102 import add, sub
def magic_calculation(x, y):
    if x < y:
        z = add(x, y)
        for a in range(4, 6):
            z = add(z, a)
        return z
    else:
        return sub(x, y)
    return 0
