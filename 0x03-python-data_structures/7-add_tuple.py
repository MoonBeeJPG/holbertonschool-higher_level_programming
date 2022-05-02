#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a > 2 and tuple_b > 2:
        my_tuple = tuple(map(lambda i, j: i + j, tuple_a[:2], tuple_b[:2]))
        return my_tuple
    elif tuple_a < 2 and tuple_b < 2:
        result =
        return my_tuple
    else:
         my_tuple = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
        return my_tuple
