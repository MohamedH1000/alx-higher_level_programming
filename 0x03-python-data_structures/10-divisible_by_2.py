#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_l = []
    for a in my_list:
        if a % 2 == 0:
            n_l.append(True)
        else:
            n_l.append(False)
    return n_l
