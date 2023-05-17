#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = dict()
    result = 0
    for a in range(len(my_list)):
        if (my_list[a] not in new_list.keys()):
            new_list[my_list[a]] = my_list[a]
            result += my_list[a]
    return (result)
