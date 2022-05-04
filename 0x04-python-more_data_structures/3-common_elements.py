#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set_1
    elements = set_2
    if (common & elements):
        return common & elements
