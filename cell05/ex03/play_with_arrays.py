#!/usr/bin/python3

# array = [2,8,9,48,8,22,-12,2]
# result = [x+2 for x in array if x >5]
# print(result)

array = [2, 8, 9, 48, 8, 22, -12, 2]
result = [x+2 for x in array if x > 5]
unique_result = list(set(result))
print("Unique elements greater than 5:", unique_result)
