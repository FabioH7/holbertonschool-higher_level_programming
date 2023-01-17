#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        val = ord(str[i])
        if val >= 97 and val <= 122:
            print("{}".format(chr(val - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
        i += 1
    print()
