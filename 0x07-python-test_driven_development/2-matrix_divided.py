#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        temporal_list = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(error)
            temporal_list.append(round(j/div, 2))
        new_matrix.append(temporal_list)
    return new_matrix
