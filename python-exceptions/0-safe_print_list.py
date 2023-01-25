#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            if i + 1 == x:
                print("{}".format(my_list[i]))
            else:
                print("{}".format(my_list[i]), end="")
    except IndexError:
        print()
        return i
    return i + 1
