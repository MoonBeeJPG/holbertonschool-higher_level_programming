#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = int(argv) - 1
    itinerate = 1
    add = 0
    
    while arguments >= itinerate:
        print(f"{int(sum(itinerate))}")
        itinerate += 1
