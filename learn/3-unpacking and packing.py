# ------
# 3. Packing and unpacking
# ------


# * is used to pack and unpack arguments
myList = [1, 2, 3, 4, 5]
print(myList) # [1, 2, 3, 4, 5] : list
print(*myList) # 1 2 3 4 5 : int int int int int


# use * to unpack a function's arguments
def printList(*args):
	for arg in args:
		print(arg)
printList(1, 2, 3, 4, 5) # 1 2 3 4 5 : int int int int int


# advanced unpacking
myList = [1, 2, 3, 4, 5]
a, b, *c = myList
print(a) # 1 : int
print(b) # 2 : int
print(c) # [3, 4, 5] : list
