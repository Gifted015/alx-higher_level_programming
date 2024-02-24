#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    for keys in sorted_dict:
        print("{}: {}".format(keys, sorted_dict[keys]))
