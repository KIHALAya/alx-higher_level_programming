#!/usr/bin/python3
def main():
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    del args[0]
    lenn = len(args)

    if lenn != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if args[1] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[0])
    b = int(args[2])
    print("{} {} {} = {}".format(a, args[1], b, operators[args[1]](a, b)))


if __name__ == "__main__":
    main()
