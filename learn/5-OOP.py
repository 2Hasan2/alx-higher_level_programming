# ----
# 5. OOP

# before OOP you have to know that everything in python is a fucking object.. OOP DONE
# ----
# OOP is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
# For instance, an object could represent a person with a name property, age, address, etc., with behaviors like walking, talking, breathing, and running.
# Or an email with properties like recipient list, subject, body, etc., and behaviors like adding attachments and sending.
# Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, etc.
# OOP models real-world entities as software objects, which have some data associated with them and can perform certain functions.
# Another common programming paradigm is procedural programming which structures a program like a recipe in that it provides a set of steps, in the form of functions and code blocks, that flow sequentially in order to complete a task.
# The key takeaway is that objects are at the center of the object-oriented programming paradigm, not only representing the data, as in procedural programming, but in the overall structure of the program as well.
# ----

# first class objects
class Member:
	# constructor - a special method that runs when an instance is created so we can set the initial state of the object
	def __init__(self, name, age):
		self.name = name
		# use __ to make the attribute private
		self.__age = age
		print("Member created: " + self.name)

	def __str__(self): # string representation of the object
		return self.name + " " + str(self.__age)

	def __del__(self): # destructor - a special method that runs when an object is destroyed
		print("Member destroyed: " + self.name)
	
	

print(dir(Member)) # list of attributes and methods of the class

# create an instance of the class
member1 = Member("John Doe", 33)
member2 = Member("Mary Jane", 25)

print(member1)
print(member2)

# delete an instance of the class
del member1
del member2


# class methods vs instance methods
class MyClass:
	# class method
	@classmethod
	def class_method(cls):
		print("Class method")

	# instance method
	def instance_method(self):
		print("Instance method")

MyClass.class_method()
# MyClass.instance_method() # error

my_class = MyClass()
my_class.instance_method()
# class method can be called by an instance : why ? because it's a class method, not an instance method ! :)
my_class.class_method()

# static methods
class MyClass:
	# static method
	@staticmethod
	def static_method():
		print("Static method")

#  static method can be called by a class or an instance
# it doesn't have access to the class or instance
# so you can use it to create a utility function like a helper function or a function that doesn't need to access the class or instance
MyClass.static_method()
my_class = MyClass()
my_class.static_method()

