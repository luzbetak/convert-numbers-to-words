#!/usr/bin/env python

from Number2Words import *


# -----------------------------------------------------------------------------#
def main(word_number):
    obj = Number2Words()
    if len(word_number) == 2:
        print(obj.hundreds(word_number))
    elif len(word_number) == 3:
        print(obj.hundreds(word_number))


# -----------------------------------------------------------------------------#
if __name__ == "__main__":
    main("456")
