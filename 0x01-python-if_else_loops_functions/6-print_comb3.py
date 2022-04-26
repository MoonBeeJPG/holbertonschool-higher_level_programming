#!/usr/bin/python3
numbercount = 0
for i in range(0, 8):
    numbercount = numbercount + 1
    for j in range(numbercount, 10):
            print("{}{}, ".format(i, j), end='')
print("89")
