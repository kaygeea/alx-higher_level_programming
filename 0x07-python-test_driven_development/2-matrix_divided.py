#!/usr/bin/python3
'''This module creates a matrix dividing function'''


def matrix_divided(matrix, div):
    '''This function divides all elements of a matrix
    Args:
        matrix: incoming argument for matrix whose elements are to be divided
        div (int or float): incoming arg by which matrix elems are to be div'd
    Exceptions:
        TypeError:
            a. if matrix is not a list of lists (i.e matrix) of ints/floats
            b. if the rows in matrix are not of the same size.
            c. if div is not a number of type int or float.
        ZeroDivisionError: if div == 0
    '''

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
