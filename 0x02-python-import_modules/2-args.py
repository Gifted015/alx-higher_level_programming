#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    num_arg = len(arguments)

    if (num_arg == 1):
        print("0 arguments.")
    else:
        if (num_arg == 2):
            print("1 argument:")
        else:
            print("{} arguments:".format(num_arg - 1))
        for i in range(1, num_arg):
            print("{}: {}".format(i, arguments[i]))
