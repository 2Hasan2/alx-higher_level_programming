# ----
# 5. OOP

# before OOP you have to know that everything in python is a fucking object.. OOP DONE :)
# ----
# OOP is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
# For instance, an object could represent a person with a name property, age, address, etc., with behaviors like walking, talking, breathing, and running.
# Or an email with properties like recipient list, subject, body, etc., and behaviors like adding attachments and sending.
# Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, etc.
# OOP models real-world entities as software objects, which have some data associated with them and can perform certain functions.
# Another common programming paradigm is procedural programming which structures a program like a recipe in that it provides a set of steps, in the form of functions and code blocks, that flow sequentially in order to complete a task.
# The key takeaway is that objects are at the center of the object-oriented programming paradigm, not only representing the data, as in procedural programming, but in the overall structure of the program as well.
# ----

# .............................................
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



# .............................................
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



# .............................................

# inheritance
# a class can inherit from another class
# the class that inherits is called child class
# the class that is inherited from is called parent class
# the child class inherits all the methods and attributes of the parent class
# the child class can override the methods of the parent class
# example
# like the cat and dog classes inherit name and speak methods from the animal class
# the animal class is the parent class
class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement abstract method")
	
class Dog(Animal):
	def speak(self):
		return self.name + " says woof!"
	
class Cat(Animal):
	def speak(self):
		return self.name + " says meow!"
	

dog = Dog("Rex")
cat = Cat("Felix")

print(dog.speak())
print(cat.speak())

# advanced inheritance
# example
class Person: #base class
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __str__(self):
		return self.name + " " + str(self.age)
	
class Employee(Person): #derived class from Person
	def __init__(self, name, age, salary):
		super().__init__(name, age)
		self.salary = salary
	
	def __str__(self):
		return super().__str__() + " " + str(self.salary)
	
class Manager(Employee): #derived class from Employee
	def __init__(self, name, age, salary, bonus):
		super().__init__(name, age, salary)
		self.bonus = bonus

	def __str__(self):
		return super().__str__() + " " + str(self.bonus)



# override 
# the derived class can override the methods of the base class
# example
class BaseOne:
	def __init__(self):
		print("BaseOne constructor")
	
	def method(self):
		print("BaseOne method")

class BaseTwo:
	def __init__(self):
		print("BaseTwo constructor")
	
	def method(self):
		print("BaseTwo method")

class Derived(BaseOne, BaseTwo):
	def __init__(self):
		super().__init__()
		print("Derived constructor")

	def method(self):
		print("Derived method")
derived = Derived()
derived.method() # BaseOne method because BaseOne is the first base class
# use the __mro__ attribute or mro() method to see the order of the base classes
print(Derived.__mro__)

# .............................................
# Polymorphism
# Polymorphism is the ability of an object to take on many forms.
# The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.
# Any Python object that implements these methods can be used in a with statement.
# The methods that are called in response to this statement are __enter__() and __exit__().
# The __enter__() method is run when execution flow enters the code block inside the with statement.
# The __exit__() method is run when execution flow leaves the code block.
# The __exit__() method can be used to end the program or to catch exceptions.
# example
# when you use len() function on a list, it returns the length of the list
len([1, 2, 3])
# when you use len() function on a string, it returns the length of the string
len("hello")
# len() function is polymorphic because it can take different forms

# example
# use polymorphism to create a class that can take different forms
# like use sum in string and num
class Int:
	def __init__(self, num):
		self.num = num
	
	def __add__(self, other):
		return self.num + other.num
	
class Str:
	def __init__(self, string):
		self.string = string
	
	def __add__(self, other):
		# convert to ASCII code and add them
		STR = self.string + other.string
		return sum([ord(char) for char in STR])

num1 = Int(1)
num2 = Int(2)
print(num1 + num2)

str1 = Str("Ha")
str2 = Str("Wa")
print(str1 + str2)

# .............................................
# Encapsulation
# Encapsulation is the process of restricting access to methods and variables in a class in order to prevent direct data modification so it prevents accidental data modification.
# To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those type of variables are known as private variable.
# and the another type of variables are known as public variables and protected variables.
# @private: __ (double underscore) before the variable name
# @protected: _ (single underscore) before the variable name
# @public: no underscore before the variable name

# example
class Person:
	def __init__(self, name, age):
		self.name = name
		self._age = age
		self.__salary = 1000

	def __str__(self):
		return self.name + " " + str(self._age) + " " + str(self.__salary)
	

person = Person("John Doe", 33)
print(person.name)
print(person._age) # you can access protected variables but it's not recommended :)
# print(person.__salary) # error


# .............................................

# Abstraction





# .............................................

# Getters and Setters
# Getters and setters are used to protect your data, particularly when creating classes.
# Getters return the value of the attribute.
# Setters let you change the value of the attribute.
# example
class Member:
	def __init__(self, name):

		self.__name = name

	# use can use name as a property and setter and getter as methods
	@property
	def get_name(self):
		return self.__name
	
	@get_name.setter
	def set_name(self, name):
		if name is not None and len(name.strip()) > 0:
			self.__name = name


member = Member("John Doe")
print(member.get_name)
member.set_name = "Mary Jane"
print(member.get_name)


# property decorator
# property decorator is used to define a property
# example
class Member:
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if name is not None and len(name.strip()) > 0:
			self.__name = name

member = Member("John Doe")
print(member.name)
# print(member.name()) # error because name is a property not a method


# .............................................

# Decorators

# .............................................

# Iterators

# .............................................

# Generators

# .............................................

# ABCs (Abstract Base Classes)
# ABCs are classes that are only meant to be inherited from, and not instantiated.
# ABCs are used to define a template for a class.

# example
# ABCs are defined in the abc module
from abc import ABCMeta , abstractmethod

class Animal(metaclass=ABCMeta):
	def __init__(self, name):
		self.name = name
	
	@abstractmethod # abstract method - it must be implemented in the derived class or it will raise an error
	def speak(self):
		pass

class Dog(Animal):
	def speak(self):
		return self.name + " says woof!"
	
class Cat(Animal):
	def speak(self):
		return self.name + " says meow!"
	pass
	

dog = Dog("Rex")
cat = Cat("Felix")

print(dog.speak())
print(cat.speak())

# .............................................

# Data Classes
# Data classes are classes that are meant to store data.
# Data classes are defined in the dataclasses module.
# Data classes are used to create classes that store data.
# Data classes are mutable.
# Data classes are like named tuples, dictionaries, and simple class but with extra features.

# example
from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int
	weight: float

person = Person("John Doe", 33, 150.5)
print(person.name)
print(person.age)
print(person.weight)

# advanced example
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
	name: str
	age: int
	weight: float
	friends: List[str] = field(default_factory=list)

person = Person("John Doe", 33, 150.5)
print(person.name)
print(person.age)
print(person.weight)
print(person.friends)
