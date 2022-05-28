#!/usr/bin/python3
""" Function that prints a text with 2 new lines after
    each one of these characters: ., ? and : """


def text_indentation(text):
    """comment"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n").replace(
            "? ", "?\n\n").replace(": ", ":\n\n")
    text = text.split("\n")

    for i in text:
        i = i.strip()
        print(i + "\n", end="")
