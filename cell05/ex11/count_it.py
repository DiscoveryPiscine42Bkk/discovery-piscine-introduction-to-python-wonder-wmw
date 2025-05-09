#!/usr/bin/env python3
import sys

# Exclude the script name itself
args = sys.argv[1:]

# Print the number of parameters
if len(args) < 1:
    print("None")
else:
    print(f"parameters: {len(args)}")

    # Print each argument and its length
    for word in args:
        print(f"{word}: {len(word)}")
