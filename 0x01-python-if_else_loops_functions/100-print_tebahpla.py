#!/usr/bin/python3
for i in range(97, 123):
    if i % 2 != 0:
        i = i - 31
    print("{:c}".format(i), end='')
