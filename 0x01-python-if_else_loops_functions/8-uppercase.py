#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char_num = ord(i)
        if (char_num >= 97 and char_num <= 122):
            char_num = char_num - 32
        print("{}".format(chr(char_num)), end="")
    print("")
