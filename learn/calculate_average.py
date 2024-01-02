#!/usr/bin/python3
def calculate_average(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(arr) / len(arr)

numbers1 = [5, 10, 15, 20]
average1 = calculate_average(numbers1)
print(average1)  # Output should be 12.5

numbers2 = []
average2 = calculate_average(numbers2)
print(average2)  # Output should be 0 (since the list is empty)