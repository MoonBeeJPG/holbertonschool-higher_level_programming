#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        string = ord(str[i])
        if string >= 97 and string <= 122:
            upper += chr(string - 32)
        else:
            upper = chr(string)
        print(f"{upper}")
