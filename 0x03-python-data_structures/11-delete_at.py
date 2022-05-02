#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        newe_list = list(my_list)
        del newe_list[idx]
        del my_list[idx]
        return newe_list
        return my_list
