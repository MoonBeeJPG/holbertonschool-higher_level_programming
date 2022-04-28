#!/usr/bin/python3
import calculator_1 as add
import calculator_1 as sub
import calculator_1 as mul
import calculator_1 as div

if __name__ == "__main__":
    a = 10
    b = 5

    addition = f"{a} + {b}"
    substraction = f"{a} - {b}"
    multiplication = f"{a} * {b}"
    division = f"{a} / {b}"

    addresult = add.add(a, b)
    subresult = sub.sub(a, b)
    mulresult = mul.mul(a, b)
    divresult = div.div(a, b)

    print(f"{addition} = {addresult}")
    print(f"{substraction} = {subresult}")
    print(f"{multiplication} = {mulresult}")
    print(f"{division} = {divresult}")
