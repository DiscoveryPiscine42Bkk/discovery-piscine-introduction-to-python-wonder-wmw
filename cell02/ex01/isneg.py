#!/usr/bin/python3
number = int(input("Please enter your numbr : "))

if number == 0:
    print("This number is both positive and negative.")
elif number < 0:
    print("This number is negative.")
else:
    print("this number is positive.")
