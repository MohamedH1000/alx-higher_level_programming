#!/usr/bin/python3
def print_last_digit(number):
    number = int(repr(number)[-1])

    print("{:d}".format(number), end="")
    return number
