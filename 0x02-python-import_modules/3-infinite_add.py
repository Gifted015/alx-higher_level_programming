#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = sys.argv
    sum = 0
    for i in range(1, len(num)):
        i = int(num[i])
        sum += i
    print("{}".format(sum))
