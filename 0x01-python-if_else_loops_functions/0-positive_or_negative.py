#!/usr/bin/python3
import random
number = random.randint(-10, 10)
n = number
print(f"{n} is {'positive' if n > 0 else 'negative' if n < 0 else 'zero'}")
