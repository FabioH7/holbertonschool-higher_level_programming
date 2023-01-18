#!/usr/bin/python3
if __name__ == "__main__":
    for item in dir('hidden_4.pyc'):
        if item[0] != "_":
            print(item)
