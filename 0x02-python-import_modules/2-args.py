#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    itinerate = 1

    if arguments == 0:
        print(f"{arguments} arguments.")
    elif arguments == 1:
        print(f"{arguments} argument:")
    else:
        print(f"{arguments} arguments:")

    while (arguments >= itinerate):
        print(f"{itinerate}: {sys.argv[itinerate]}")
        itinerate += 1
