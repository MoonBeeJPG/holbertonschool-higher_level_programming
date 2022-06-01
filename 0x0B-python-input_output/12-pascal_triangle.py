#!/usr/bin/python3
""" a function that returns a list of lists of integers
    representing the Pascal's triangle of n """


def pascal_triangle(n):
    """ prototype defined """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    new_list = [[1]]
    for i in range(n-1):
        list = [1]
        for j in range(i):
            list.append(new_list[-1][i] + new_list[-1][i+1])

        list.append(1)
        new_list.append(list)

    return new_list
