#!/usr/bin/python3

def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def division(a, b):
    return a/b
def multiplication(a, b):
    return a*b

first = int(input("Give me the first number : "))
second = int(input("Give me the second number : "))
print("Thank you!!")

print(f"{first} + {second} = {addition(first, second)}")
print(f"{first} - {second} = {subtraction(first, second)}")
print(f"{first} / {second} = {division(first, second)}")
print(f"{first} * {second} = {multiplication(first, second)}")