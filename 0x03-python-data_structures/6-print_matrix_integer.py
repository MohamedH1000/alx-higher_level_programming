#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function that prints a mat of integers"""
    for r in matrix:
        for a in r:
            if a != r[-1]:
                print("{:d}".format(a), end=" ")
            else:
                print("{:d}".format(a), end="")
        print()
