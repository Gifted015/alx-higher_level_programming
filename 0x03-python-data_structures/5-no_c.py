#!/usr/bin/python3
def no_c(my_string):
    new = []
    for x in range(len(my_string)):
        if my_string[x] == 'c' or my_string[x] == 'C':
            continue
        else:
            new.append(my_string[x])
    new = "".join(new)
    return new
