#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_original = list(my_list)
    if idx >= len(my_list):
        return cp_original
    elif idx < 0:
        return cp_original
    else:
        new_my_list = list(my_list)
        new_my_list[idx] = element
        return new_my_list
