#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        rev_list = my_list[::-1]
        for num in rev_list:
            print("{:d}".format(num))
