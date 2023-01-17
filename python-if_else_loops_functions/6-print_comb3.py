#!/usr/bin/python
for i in range(0, 9):
    for j in range(1, 10):
        if i + j == 17:
            print("{}{}".format(i, j))
        elif i != j and i < j:
            print("{}{}".format(i, j), end=", ")
