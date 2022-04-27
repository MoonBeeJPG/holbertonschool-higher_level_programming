#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 15 == 0:
            print("FizzBuzz ", end='')
            continue
        elif i % 3 == 0:
            print("Fizz ", end='')
            continue
        elif i % 5 == 0:
            print("Buzz ", end='')
            continue
        print(f"{i} ", end='')
    print("Buzz")
