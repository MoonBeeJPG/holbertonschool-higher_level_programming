#!/usr/bin/python3
""" Function that prints a text with 2 new lines after
    each one of these characters: ., ? and : """


def text_indentation(text):
    """comment"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chr1 = text.replace(". ", ".\n\n").replace(
            "? ", "?\n\n").replace(": ", ":\n\n")
    chr1 = text.split("\n")

    for i in chr1:
        i = i.strip()
        print(i + "\n", end="")
