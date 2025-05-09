#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("None")
else:    
    for i in reversed(sys.argv):
        print(i)
    
    
