#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return(0)
    a = 0
    b = 0
    for x in range(len(my_list)):
        for y in range(len(my_list)):
            a = a + (my_list[x][y] * my_list[x][y+1])
            b = b + my_list[x][y+1]
            break
    return(a / b)
