#!/usr/bin/python3
def convertor(value):
    if value == 'I':
        return 1
    if value == 'V':
        return 5
    if value == 'X':
        return 10
    if value == 'L':
        return 50
    if value == 'C':
        return 100
    if value == 'D':
        return 500
    if value == 'M':
        return 1000
    return 0


def roman_to_int(roman_string):
    i = 0
    result = 0
    if not roman_string:
        return 0
    if roman_string.isdigit():
        return 0
    while (i < len(roman_string)):
        current = convertor(roman_string[i])

        if i + 1 < len(roman_string):
            next_s = convertor(roman_string[i + 1])

            if current >= next_s:
                result += current
                i += 1
            else:
                result += next_s - current
                i += 2
        else:
            result += current
            i += 1
    return result
