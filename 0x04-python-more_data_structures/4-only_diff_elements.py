#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    first = set_1
    second = set_2
    if first ^ second:
        return first ^ second
