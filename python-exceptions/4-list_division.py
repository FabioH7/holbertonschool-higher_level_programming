#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    try:
        while i < list_length:
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
            i += 1
    finally:
        return new_list
