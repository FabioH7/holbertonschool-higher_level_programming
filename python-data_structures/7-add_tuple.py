#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a0 = 0
        a1 = 0
    elif len(tuple_a) == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if len(tuple_b) == 0:
        b0 = 0
        b1 = 0
    elif len(tuple_b) == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    sum_a = a0 + b0
    sum_b = a1 + b1
    new_tuple = (sum_a, sum_b)
    return new_tuple
