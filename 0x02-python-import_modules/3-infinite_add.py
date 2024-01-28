#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = sys.argv
    sum = 0
    for i in num:
        i = int(i)
        sum += i
    print("{}".format(sum))
