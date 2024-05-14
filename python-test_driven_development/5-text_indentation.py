#!/usr/bin/python3
'''This module splits text after each ".?:"'''


def text_indentation(t):
    '''Print text with 2 new lines after each ".?:"

        Args:
            text (str): text to split

        Raises:
            TypeError: text must be a string
    '''

    err_message = "text must be a string"

    if not isinstance(t, str):
        raise TypeError(err_message)

    t = t.replace(".", ".\n\n").replace(":", ":\n\n").replace("?", "?\n\n")
    p = t.splitlines(True)
    t_array = []
    for line in p:
        if line == "\n":
            t_array.append("\n")
        else:
            t_array.append(line.lstrip())
    print("".join(t_array), end="")
