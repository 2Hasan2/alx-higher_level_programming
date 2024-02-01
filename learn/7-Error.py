# ---------
#  7. Error handling
# ---------

# raise 

##  Exception handling
# raise Exception('This is the error message.')


##  ValueError
# raise ValueError('This is the error message.')


##  AssertionError
# assert False, 'This is the error message.'


##  try and except statements
num = 1
try: # try block ... it will try this code
	print(1 / num)
except: # except block ... if there is an error, it will execute this code
	print('Error: Invalid argument.')
else: # else block ... if there is no error, it will execute this code
	print("This is executed from else after try block")
finally: # finally block ... it will execute this code no matter what
	print("This is executed finally")

# use except ERRORTYPE to catch specific error
# ERRORTYPE like [ZeroDivisionError, TypeError, NameError, ValueError, AssertionError]
try:
	print(1 / 0)
except ZeroDivisionError:
	print('Error: Invalid argument.')
	

# advanced error handling
the_file = None
the_tries = 5

try:
	while the_tries > 0:
		try:
			the_file = open(input('input file name:'), 'r')
		except FileNotFoundError as e:
			the_tries -= 1
			print(str(e.args[1]), f'left {the_tries} tries')
		else:
			print('File opened successfully')
			break
finally:
	print('This is executed finally')

