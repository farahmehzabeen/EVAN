# Array Methods: Python has a set of built-in methods that you can use on lists/arrays.

# Adding Array Elements: You can use the append() method to add an element to an array.
# The append() method appends an element to the end of the list.
# Syntax -> list.append(element)
# Parameter -> element; Description -> Required. An element of any type (string, number, object etc.)
# Example
# Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

a = ["apple", "banana", "cherry"]
b = ("Ford", "BMW", "Volvo")
a.append(b)
print(a)
print(len(a))

# The clear() method removes all the elements from a list.
# Syntax -> list.clear()
# No parameters
# Example
# Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# The copy() method returns a copy of the specified list.
# Syntax -> list.copy()
# No parameters
# Example
# Copy the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# The count() method returns the number of elements with the specified value.
# Syntax -> list.count(value)
# Parameter -> value; Description -> Required. Any type (string, number, list, tuple, etc.). The value to search for.
# Example
# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.count("cherry")
print(x)
# Example
# Return the number of times the value 9 appears int the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
# Syntax -> list.extend(iterable)
# Parameter -> iterable	Description -> Required. Any iterable (list, set, tuple, etc.)
# Example
# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# Example
# Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# The index() method returns the position at the first occurrence of the specified value.
# Syntax -> list.index(element)
# Parameter -> element;	Description -> Required. Any type (string, number, list, etc.). The element to search for
# Example
# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.index("cherry")
print(x)

# Example
# What is the position of the value 32:
points = [4, 55, 64, 32, 16, 32]
x = points.index(32)
print(x)
# Note: The index() method only returns the first occurrence of the value.

# The insert() method inserts the specified value at the specified position.
# Syntax -> list.insert(position, element)
# Parameter	-> position; Description -Required. A number specifying in which position to insert the value
# Parameter	-> element;	Description -> Required. An element of any type (string, number, object etc.)
# Example
# Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# The pop() method removes the element at the specified position.
# Syntax -> list.pop(position)
# Parameter -> position; Description -> Optional. A number specifying the position of the element you want to remove,
# default value is -1, which returns the last item
# Removing Array Elements: You can use the pop() method to remove an element from the array.
# Example
# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

# Example
# Return the removed element:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop()
print(x)

# You can also use the remove() method to remove an element from the array.
# Example
# Delete the element that has the value "Volvo":
cars.remove("Volvo")
# Note: The list's remove() method only removes the first occurrence of the specified value.

# The reverse() method reverses the sorting order of the elements.
# Syntax -> list.reverse()
# No parameters
# Example
# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax -> list.sort(reverse=True|False, key=myFunc)
# Parameter -> reverse; Description -> Optional. reverse=True will sort the list descending. Default is reverse=False
# Parameter	-> key; Description -> Optional. A function to specify the sorting criteria(s)
# Example
# Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
# Example
# Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)


# Example
# Sort the list by the length of the values:
# # A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
print(cars)


# Example
# Sort a list of dictionaries based on the "year" value of the dictionaries:
# # A function that returns the 'year' value:
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
# # A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)


def function6(e):
    return len(e)


array = ["kiwi", "strawberry", "banana", "apple", "orange", "tomato", "grape"]
array.sort(reverse=True, key=function6)
print(array)
