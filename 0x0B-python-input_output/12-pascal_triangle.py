#!/usr/bin/python3
"""
pascal triangle module method
"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers
    """
    r = [[1 for b in range(a + 1)] for a in range(rg)]
    for rg in range(rg):
        for a in range(rg - 1):
            r[rg][a + 1] = sum(r[rg - 1][a:a + 2])
    return r
