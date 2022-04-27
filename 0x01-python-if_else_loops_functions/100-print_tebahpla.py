#!/usr/bin/python3
for i in range(96, 123):
    if i % 2 != 0:
        i = - 31
    print("{:c}".format(i), end='')
