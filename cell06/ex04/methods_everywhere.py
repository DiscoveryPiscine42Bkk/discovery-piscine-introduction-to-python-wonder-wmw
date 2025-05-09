#!/usr/bin/env python3

def shrink(word):
    print(word[:8])

def slices(word):
    print(word[:8])

def enlarge(text):
    if not isinstance(text, str):
        print("Error: Input must be a string.")
    else:
        enlarged_text = text.ljust(8, 'Z')  
        print(enlarged_text)

import sys

args = sys.argv[1:]

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(len(args)):
        if len(args[i]) < 8:
            print(enlarge(args[i]))
        elif len(args[i]) > 8:
            print(shrink(args[i]))
        else:
            print(args[i])

