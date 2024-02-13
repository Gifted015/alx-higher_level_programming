#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    i = 0
    str_len = len(str_list)
    while (i < str_len):
        print(i)
        if (str_list[i] == 'c' or str_list[i] == 'C'):
            str_list.remove(str_list[i])
            str_len -= 1
        else:
            i += 1
    new_str = "".join(str_list)
    return (new_str)
