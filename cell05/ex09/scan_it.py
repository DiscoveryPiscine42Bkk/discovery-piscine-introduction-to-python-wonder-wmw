#!/usr/bin/python3

import sys, re

if len(sys.argv) < 2:
    print("none")
else:
    count = len(re.findall(sys.argv[1], sys.argv[2]))
    print(count)
