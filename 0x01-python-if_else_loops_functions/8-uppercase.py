#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char_num = ord(i)
        if (char_num >= 97 and char_num <= 122):
            print("{}".format(chr(char_num - 32)), end="")
        else:
            print("{}".format(chr(char_num)), end="")
    print("")