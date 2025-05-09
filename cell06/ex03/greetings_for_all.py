#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error: Name must be a string.")
    else:
        print(f"Welcome, {name}!")

greetings()
greetings("Alice")
greetings(2343)