# -----
# 4. Lambda
# -----

# lambda is an anonymous function
# lambda arguments : expression

# example 1
print((lambda x : x + 1)(2)) # 3 : int

# example 2
add = lambda x, y : x + y
print(add(2, 3)) # 5 : int

# example 3
# lambda functions can be used as arguments
myList = [1, 2, 3, 4, 5]
print(list(map(lambda x : x + 1, myList))) # [2, 3, 4, 5, 6] : list

# example 4
# lambda functions can be used as arguments
myList = [1, 2, 3, 4, 5]
print(list(filter(lambda x : x % 2 == 0, myList))) # [2, 4] : list

# name of the function is <lambda>
print((lambda x : x + 1).__name__) # <lambda> : str
