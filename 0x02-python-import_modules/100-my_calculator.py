#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arguments = len(sys.argv) - 1

    if arguments != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    print(f"{a} {operator} {b} = {result}")
