#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    num_arg = len(arguments)

    if (num_arg == 0):
        print("0 argument.")
    else:
        if (num_arg == 1):
            print("1 argument:")
        else:
            print("{} arguments:".format(num_arg))
        for i in range(0, num_arg):
            print("{}: {}".format(arguments[i]))
