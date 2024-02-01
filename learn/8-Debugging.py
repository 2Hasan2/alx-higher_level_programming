# ---------------------
#  8. Debugging
# ---------------------

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for num in my_list:
	print(num)

for key, value in my_dict.items():
	print(f'{key} => {value}')

def my_function():
	print('This is a function')

my_function()