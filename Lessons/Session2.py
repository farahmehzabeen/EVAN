import random


# There are three numeric types in Python: int, float, complex
# Variables of numeric types are created when you assign a value to them:
x = 1  # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function:
print(type(x))
print(type(y))
print(type(z))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x1 = 1
y1 = 35656222554887711
z1 = -3255522

print(type(x1))
print(type(y1))
print(type(z1))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x2 = 1.10
y2 = 1.0
z2 = -35.59

print(type(x2))
print(type(y2))
print(type(z2))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x3 = 35e3
y3 = 12E4
z3 = -87.7e100

print(type(x3))
print(type(y3))
print(type(z3))

# Complex numbers are written with a "j" as the imaginary part: You cannot convert complex numbers into another number
# type.
x4 = 3+5j
y4 = 5j
z4 = -5j

print(type(x4))
print(type(y4))
print(type(z4))

# Type Conversion - convert from one type to another with the int(), float(), and complex() methods.
# convert from int to float
a = float(x)

# convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Python does not have a random() function to make a random number, but Python has a built-in module called random that
# can be used to make random numbers.

# In Python, Modules are simply files with the “.py” extension containing Python code that can be imported inside
# another Python Program.
# In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions
# that you want to include in your application.

# Import the random module, and display a random number between 1 and 9
print(random.randrange(10, 20))


# Casting means to specify a Variable Type; uses classes to define data types, including its primitive types.

# Primitive Data Structures – These data structures contain simplified data values and serve as the foundation for
# manipulating data. The four primitive data structures are integers, float, string, and boolean.

# Non-primitive Data Structures – These data structures store values, as well as a collection of values, in varying
# formats. The four built-in non-primitive data structures are lists, tuples, dictionaries, and sets.


# Primitive data types: In computer science, primitive data types are a set of basic data types from which all other
# data types are constructed.
# Specifically it often refers to the limited set of data representations in use by a particular processor, which all
# compiled programs must use.


# Casting in python is done using constructor functions


# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string
# literal (providing the string represents a whole number)

# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string
# represents a float or an integer)

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


# Integers:
x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # what will z be?


# Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


# Strings:

x = str("s1") # x will be "s1"
y = str(2)    # y will be  "2"
z = str(3.0)  # z will be  "3.0"

print(x, y, z)
print(9 / 3)