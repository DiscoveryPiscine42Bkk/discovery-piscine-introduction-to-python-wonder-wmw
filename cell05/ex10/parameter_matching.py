#!/usr/bin/python3
import sys

if (len(sys.argv)) < 2:
    print("none")
else:
    input_param = input("What was the parameters? ")
    if (input_param == sys.argv[1]):
        print("Good Job!!")
    else:
        print("Nope, Sorry....")
