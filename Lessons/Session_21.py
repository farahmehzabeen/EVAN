# Python Arrays
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#
# Arrays
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import
# a library, like the NumPy library.
#
# Arrays are used to store multiple values in one single variable:
#
# Example
# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW", "Volvo"]

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
#
# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like
# this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
#
# The solution is an array!
#
# An array can hold many values under a single name, and you can access the values by referring to an index number.
#
# Access the Elements of an Array
# You refer to an array element by referring to the index number.
#
# Example
# Get the value of the first array item:

x = cars[0]
# Example
# Modify the value of the first array item:

cars[0] = "Toyota"
# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
#
# Example
# Return the number of elements in the cars array:

x = len(cars)
# Note: The length of an array is always one more than the highest array index.

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
#
# Example
# Print each item in the cars array:

for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
#
# Example
# Add one more element to the cars array:

cars.append("Honda")
print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
#
# Example
# Delete the second element of the cars array:

cars.pop(1)
print(cars)

# You can also use the remove() method to remove an element from the array.
#
# Example
# Delete the element that has the value "Volvo":

cars.remove("Volvo")
print(cars)

# Note: The list's remove() method only removes the first occurrence of the specified value.
#
# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.
#
# Method	Description
# append()	Adds an element at the end of the list

# Example
# Add an element to the fruits list:

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# Definition and Usage
# The append() method appends an element to the end of the list.
# Syntax : list.append(elmnt)
# Parameter Values	Description
# elmnt	Required. An element of any type (string, number, object etc.)

# Example
# Add a list to a list:

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.extend(b)
print(a)
print(len(a))

# clear()	Removes all the elements from the list

# Example
# Remove all elements from the fruits list:

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

# Definition and Usage
# The clear() method removes all the elements from a list.
# Syntax: list.clear()
# No parameters


# copy()	Returns a copy of the list

# Example
# Copy the fruits list:

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# Definition and Usage
# The copy() method returns a copy of the specified list.
# Syntax : list.copy()
# No parameters

# count()	Returns the number of elements with the specified value

# Example
# Return the number of times the value "cherry" appears in the fruits list:

fruits = ['apple', 'banana', 'cherry', 'cherry', 'cherry']
x = fruits.count("cherry")
print(x)

# Definition and Usage
# The count() method returns the number of elements with the specified value.
# Syntax : list.count(value)
# Parameter Values	Description
# value	Required. Any type (string, number, list, tuple, etc.). The value to search for.

# Example
# Return the number of times the value 9 appears int the list:

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# extend()	Add the elements of a list (or any iterable), to the end of the current list

# Example
# Add the elements of cars to the fruits list:

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# Definition and Usage
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
# Syntax : list.extend(iterable)
# Parameter Values	Description
# iterable	Required. Any iterable (list, set, tuple, etc.)
# Example
# Add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# index()	Returns the index of the first element with the specified value

# Example
# What is the position of the value "cherry":

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# Definition and Usage
# The index() method returns the position at the first occurrence of the specified value.
# Syntax : list.index(elmnt)
# Parameter Values	Description
# elmnt	Required. Any type (string, number, list, etc.). The element to search for

# Example
# What is the position of the value 32:

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

# Note: The index() method only returns the first occurrence of the value.

# insert()	Adds an element at the specified position

# Example
# Insert the value "orange" as the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# Definition and Usage
# The insert() method inserts the specified value at the specified position.
# Syntax : list.insert(pos, elmnt)
# Parameter Values	Description
# pos	Required. A number specifying in which position to insert the value
# elmnt	Required. An element of any type (string, number, object etc.)

# pop()	Removes the element at the specified position

# Example
# Remove the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits)

# Definition and Usage
# The pop() method removes the element at the specified position.
# Syntax : list.pop(pos)
# Parameter Values	Description
# pos	Optional. A number specifying the position of the element you want to remove, default value is -1, which returns
# the last item

# Example
# Return the removed element:

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

# Note: The pop() method returns removed value.

# remove()	Removes the first item with the specified value

# Example
# Remove the "banana" element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# Definition and Usage
# The remove() method removes the first occurrence of the element with the specified value.
#  Syntax : list.remove(elmnt)
# Parameter Values, Description
# elmnt	Required. Any type (string, number, list etc.) The element you want to remove

# reverse()	Reverses the order of the list

# Example
# Reverse the order of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# Definition and Usage
# The reverse() method reverses the sorting order of the elements.
# Syntax : list.reverse()
# No parameters

# The built-in function reversed() returns a reversed iterator object.

# sort()	Sorts the list

# Example
# Sort the list alphabetically:

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# Definition and Usage
# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax : list.sort(reverse=True|False, key=myFunc)
# Parameter Values, Description
# reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
# key	Optional. A function to specify the sorting criteria(s)

# Example
# Sort the list descending:

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)


# Example
# Sort the list by the length of the values:

# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


# Example
# Sort a list of dictionaries based on the "year" value of the dictionaries:

# A function that returns the 'year' value:
def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)


# Example
# Sort the list by the length of the values and reversed:

# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
