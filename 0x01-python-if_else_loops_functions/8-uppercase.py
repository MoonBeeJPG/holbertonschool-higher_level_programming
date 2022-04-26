#!/usr/bin/python3
def uppercase(str):
    i = 0
    upper = ''
    while str[i:]:
        string = ord(str[i])
        if string >= 67 and string <= 122:
            upper += chr(string - 32)
        else:
            upper += chr(string)
        i += 1
    print(f"{upper}")

