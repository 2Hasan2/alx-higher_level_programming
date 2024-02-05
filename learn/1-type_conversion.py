# -----
# -- 1. Type Conversion
# -----

# str() - converts to string
a = 14
b = str(a)
print(b, type(b))

# int() - converts to integer
a = "14"
b = int(a)
print(b, type(b))


# float() - converts to float
a = "14"
b = float(a)
print(b, type(b))

# bool() - converts to boolean
a = "14"
b = bool(a)
print(b, type(b))

# list() - converts to list
a = "14"
b = list(a)
print(b, type(b))


# tuple() - converts to tuple
a = "14"
b = tuple(a)
print(b, type(b))

# set() - converts to set
a = "14"
b = set(a)
print(b, type(b))


# dict() - converts to dictionary , must include key and value
a = ["14", "15", "16"]
b = dict(a)
print(b, type(b))

# frozenset() - converts to frozen set
a = "14"
b = frozenset(a)
print(b, type(b))


# chr() - converts to character
a = 14
b = chr(a)
print(b, type(b))

# ord() - converts to integer . it only accepts a single character 
a = "1"
b = ord(a)
print(b, type(b))

# hex() - converts to hexadecimal
a = 14
b = hex(a)
print(b, type(b))

# oct() - converts to octal
a = 14
b = oct(a)
print(b, type(b))


# type hinting
def add(a: int, b: int) -> int:
	return a + b

print(add(1, 2))

# type hinting with list
from typing import List
def add(a: List[int]) -> int:
	return sum(a)

