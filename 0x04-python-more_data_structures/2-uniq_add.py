#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(0, len(my_list)):
        check = 0
        for j in range(0, i):
            if (my_list[i] == my_list[j]):
                check += 1
        if (check > 0):
            continue
        else:
            sum += my_list[i]
    return (sum)
