#!/usr/bin/python3
'''This module splits text after each ".?:"'''


def text_indentation(text):
    '''Print text with 2 new lines after each ".?:"

        Args:
            text (str): text to split

        Raises:
            TypeError: text must be a string
    '''

    err_message = "text must be a string"

    if not isinstance(text, str):
        raise TypeError(err_message)

    for word in text:
        if word == "." or word == "?" or word == ":":
            print(word + "\n\n", end="")
        else:
            print("{}".format(word), end="")
