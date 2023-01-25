#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            if i + 1 == x:
                print("{}".format(my_list[i]))
            else:
                print("{}".format(my_list[i]), end="")
            i += 1
    except IndexError:
        print()
        return i
    return i + 1
