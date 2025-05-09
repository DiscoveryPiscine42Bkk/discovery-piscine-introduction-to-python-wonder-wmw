#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    z_string = ""
    for char in sys.argv[1]:
        if char == 'z':
            z_string += char
    print(z_string)

