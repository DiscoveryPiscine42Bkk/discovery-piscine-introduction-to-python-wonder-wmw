#!/usr/bin/env python3

def array_of_names(name_dict):  

    full_names = []
    for first, last in name_dict.items():
        if isinstance(first, str) and isinstance(last, str):
            full_name = f"{first.capitalize()} {last.capitalize()}"
            full_names.append(full_name)
    return full_names

names = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi" : "brindacier"
}

result = array_of_names(names)
print(result)
