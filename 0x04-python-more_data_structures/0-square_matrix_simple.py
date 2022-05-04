#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        mapping = map(lambda x: x * x, matrix[i])
        new_matrix.append(list(mapping))
    return new_matrix
