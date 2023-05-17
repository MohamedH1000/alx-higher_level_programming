#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for a in range(len(my_list)):
        if new_list[a] == search:
            new_list[a] = replace
        else:
            new_list[a] = my_list[a]
    return(new_list)
