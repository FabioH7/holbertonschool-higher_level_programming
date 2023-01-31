#!/usr/bin/python3
def text_indentation(text):
    char = ['.', '?', ':']
    i = 0
    while i in range(len(text)):
        print('{}'.format(text[i]), end="")
        if text[i] in char:
            print('\n')
            if text[i + 1] == " ":
                i += 1
        i += 1
