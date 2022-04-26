#!/usr/bin/python3
def uppercase(str):
    for i in str:
        string = ord(i)
        if  string >= 67 and string < 123:
            i = ord(i) - 32
            i= chr(i)
        print(f"{i}", end='')
    print("")

