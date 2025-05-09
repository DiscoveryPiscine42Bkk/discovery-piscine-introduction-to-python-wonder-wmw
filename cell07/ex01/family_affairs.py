#!/usr/bin/env python3

def find_the_redheads(family):
    red = []
    for name in family:
        hair_color = family[name]
        if hair_color.lower() == "red":
            red.append(name)
    return red

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))