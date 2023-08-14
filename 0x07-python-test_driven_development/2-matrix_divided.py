#!/usr/bin/python3
"""
    a function that divides a matrix
"""
def matrix_divided(matrix, div):
    """ a number div to divide a matrix """
    list_error = "list og integer or floats matrix must be a matrix"
    len_error = "the matrix should have the same size of each row"
    div_error_int = "the number to be divided must be an integer"
    div_error_zero = "the matrix to be divided by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_error_int)
    if div == 0:
        raise ZeroDivisionError(div_error_zero)
    alongitude = len(matrix[0])
    for list_a in matrix:
        if type(list_a) is not list:
            raise TypeError(list_error)
        if len(list_a) != alongitude:
            raise TypeError(len_error)
        for item in list_a:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            number = item / div
            new_list.append(round(number, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
