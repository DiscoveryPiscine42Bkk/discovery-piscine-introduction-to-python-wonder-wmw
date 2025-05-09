#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args)!=2:
    print("none")
else:
    result = list(range(int(args[0]), int(args[1])))
    print(result)