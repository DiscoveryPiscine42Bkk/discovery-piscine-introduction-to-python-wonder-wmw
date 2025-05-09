#!/usr/bin/python3

import sys

# Exclude the script name itself (sys.argv[0])
num_parameters = len(sys.argv) - 1

print(f"Number of parameters: {num_parameters}.")
