#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_l = []
    dx = 0
    while dx < list_length:
        try:
            res = my_list_1[dx] / my_list_2[dx]
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        finally:
            n_l += [res]
        dx += 1
    return n_l
