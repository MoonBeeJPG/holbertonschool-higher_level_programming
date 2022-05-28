#!/usr/bin/python3
""" Function that prints a text with 2 new lines after
    each one of these characters: ., ? and : """


def text_indentation(text):
    """comment"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chr1 = text.replace(". ", ".\n\n")
    chr2 = chr1.replace("? ", "?\n\n")
    chr3 = chr2.replace(": ", ":\n\n")
    print(chr3, end="")
