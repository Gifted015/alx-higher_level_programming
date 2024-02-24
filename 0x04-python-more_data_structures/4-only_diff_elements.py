#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for i in set_1:
        check = 0
        for j in set_2:
            if (i == j):
                check += 1
        if (check == 0):
            diff.add(i)

    for i in set_2:
        check = 0
        for j in set_1:
            if (i == j):
                check += 1
        if (check == 0):
            diff.add(i)

    return (diff)
