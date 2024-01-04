#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    try:
        a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    except ValueError:
        print("Invalid input. Please provide integer values for <a> and <b>.")
        sys.exit(1)

    try:
        result = {
            '+': add(a, b),
            '-': sub(a, b),
            '*': mul(a, b),
            '/': div(a, b)
        }.get(operator, "Unknown operator. Available operators: +, -, * and /")

        print("{} {} {} = {}".format(a, operator, b, result))
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)
