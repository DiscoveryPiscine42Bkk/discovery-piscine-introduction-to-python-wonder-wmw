#!/usr/bin/env python3

def average(classroom):
    total = 0
    count = 0
    for score in classroom.values():
        total += score
        count += 1
    return total / count 


class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
