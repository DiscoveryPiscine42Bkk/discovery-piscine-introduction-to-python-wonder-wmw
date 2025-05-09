#!/usr/bin/python3

def checkSign(number):
    if number == 0:
        print("This number is both positive and negative.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("this number is positive.")

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

result = a * b
print(a, "x", b, "=", result)
checkSign(result)

