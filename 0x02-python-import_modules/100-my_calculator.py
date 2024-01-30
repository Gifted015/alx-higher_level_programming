#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    arg.pop(0)
    arg_num = len(arg)
    op = ['+', '-', '*', '/']

    if (arg_num < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif (arg[1] not in op):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        a = int(arg[0])
        b = int(arg[2])
        comd = [add(a, b), sub(a, b), mul(a, b), div(a, b)]

        for i in range(0, 4):
            if (arg[1] == op[i]):
                c = comd[i]
                break

        print("{} {} {} = {}".format(a, arg[1], b, c))
