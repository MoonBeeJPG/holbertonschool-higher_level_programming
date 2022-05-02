#!/usr/bin/python3
def no_c(my_string):
    cC = {'c': None, 'C': None}
    making = my_string.maketrans(cC)
    new = my_string.translate(making)
    return new
