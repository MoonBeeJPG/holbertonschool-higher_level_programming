#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv)
    addition = 0

    for i in range(1, arguments):
        addition += int(sys.argv[i])
    print(f"{addition}")
