#!/usr/bin/env python

from Number2Words import *


# -----------------------------------------------------------------------------  #
def main(word_number):
    obj = Number2Words()
    if len(word_number) == 1:
        print(obj.unit(word_number))
    elif len(word_number) == 2:
        print(obj.tens(word_number))
    elif len(word_number) == 3:
        print(obj.hundreds(word_number))
    elif len(word_number) == 4:
        print(obj.thousands(word_number))

# -----------------------------------------------------------------------------  #
if __name__ == "__main__":

    main("1")
    main("12")
    main("123")
    main("1234")