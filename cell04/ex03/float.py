#!/usr/bin/python3

number = input("Give me a number: ")

num = float(number)

# Check if it's an integer (e.g. 42.0 is still an integer)
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")

