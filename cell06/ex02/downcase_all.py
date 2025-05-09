#!/usr/bin/python3

import sys

def downcase_all(args):
    for arg in args:
        print(arg.lower())

downcase_all(sys.argv[1:])
