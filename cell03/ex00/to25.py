#!/usr/bin/python3

number = int(input("Enter a number less than 25 : "))

if number > 25:
    print("The number is larger than 25.")
while number <= 25:
    print("Inside the loop, my variable is", number)
    number += 1


