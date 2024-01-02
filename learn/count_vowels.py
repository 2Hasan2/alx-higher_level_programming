#!/usr/bin/python3

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count




text1 = "Hello, World!"
count1 = count_vowels(text1)
print(count1)  # Output should be 3 (o, e, o are vowels)

text2 = "Python is amazing"
count2 = count_vowels(text2)
print(count2)  # Output should be 6 (o, i, a, i, a, i are vowels)
