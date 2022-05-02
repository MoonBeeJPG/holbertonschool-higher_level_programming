#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > 0:
        if idx <= len(my_list):
            new_my_list = list(my_list)
            new_my_list[idx] = element
            return new_my_list
