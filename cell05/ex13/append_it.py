#!/usr/bin/env python3

import sys
args = sys.argv[1:]

if len(args) < 1:
    print("none")
else:
    for i in range(len(args)):
        if args[i][-3:] != "ism":
            print(f"{args[i]}ism")
        

