#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    lstdigit = number % 10
else:
    lstdigit = number % -10

if lstdigit < 6 and lstdigit != 0:
    print(f"Last digit of {number} is {lstdigit} and is less than 6 and not 0")
elif lstdigit < 5:
    print(f"Last digit of {number} is {lstdigit} and is greather than 5")
else lstdigit == 0:
    print(f"Last digit of {number} is {lstdigit} and is zero")
