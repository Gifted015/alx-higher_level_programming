#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    i = 0
    str_len = len(str_list)
    while (i < str_len):
        if (str_list[i] == 'c' || str_list[i] == 'C'):
            str_list.pop(i)
            str_len -= 1
        i += 1
    new_str = "".join(str_list)
    return (new_str)
