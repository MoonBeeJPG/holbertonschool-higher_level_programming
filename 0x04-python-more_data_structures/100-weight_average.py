#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numer = 0
        oper = 0
        for i in my_list:
            numer += i[0] * i[1]
            oper += i[1]
        return numer / oper
    else:
        return 0
