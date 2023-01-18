#!/usr/bin/python3
for item in dir('hidden_4.pyc'):
    if item[0] != "_":
        print(item)
