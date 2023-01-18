#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    while i < len(sys.argv):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
