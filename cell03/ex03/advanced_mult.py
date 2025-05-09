#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    row = 0
    while row <= 10:
        print(f"Table de {row} :", end = " ")
        col = 0 
        while col <= 10:
            print(f"{row * col}", end = " ")
            col += 1
        print()
        row += 1 
  