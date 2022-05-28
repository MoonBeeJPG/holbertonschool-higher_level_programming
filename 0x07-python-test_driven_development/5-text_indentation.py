#!/usr/bin/python3
""" Function that prints a text with 2 new lines after
    each one of these characters: ., ? and : """


def text_indentation(text):
    """comment"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    ch1 = text.replace(". ", ".\n\n")
    ch2 = text.replace("? ", "?\n\n")
    chr3 = text.replace(": ", ":\n\n")
    print(chr3, end="")
