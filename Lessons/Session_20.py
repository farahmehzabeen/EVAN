# Python Lambda Functions
# A lambda function is a small, anonymous function in Python. Unlike regular functions that are defined using the def
# keyword, lambda functions are defined using the lambda keyword.

# Key Characteristics:
# Anonymous: Lambda functions do not have a name.
# Single Expression: They can only contain a single expression, which is evaluated and returned.
# Multiple Arguments: Lambda functions can take any number of arguments.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned.

# Example
# Add 10 to argument a, and return the result:

x = lambda a: a + 10
print(x(5))  # Output: 15

# Lambda functions can take any number of arguments.
# Example
# Multiply argument a with argument b and return the result:

x = lambda a, b: a * b
print(x(5, 6))  # Output: 30

# Summation of arguments a, b, and c and return the result:

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions?
# Lambda functions are particularly useful when you need a small function for a short period. They are often used as
# arguments to higher-order functions, which are functions that take other functions as arguments.

# Using Lambda Functions Inside Another Function
# You can use lambda functions within another function to create small, customizable functions.

# Example 1: Doubling Numbers
# Let's define a function myfunc that takes one argument n. This function will return a lambda function that multiplies
# any given number by n.

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))  # Output: 22


# Example 2: Tripling Numbers
# Similarly, you can create a function that triples any given number.

def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))


# Example 3: Using Both Doubling and Tripling Functions
# You can create both functions in the same program.

def myfunc(n):
  return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  # Output: 22
print(mytripler(11))  # Output: 33

# Practical Uses of Lambda Functions
# Sorting: You can use lambda functions to customize the sorting order.

points = [(1, 2), (3, 1), (5, -1)]
points.sort(key=lambda point: point[1])
print(points)  # Output: [(5, -1), (3, 1), (1, 2)]

# Here, the 'key' parameter is used to specify a function that will be called on each element in the list to determine
# the value to be used for sorting.
# lambda takes one argument, point, which represents each tuple in the list.
# point[1] extracts the second element (y-coordinate) from each tuple.
# The sort() method uses these y-coordinates to sort the list of tuples.

# Filtering: You can use lambda functions with the filter function to filter out elements from a list.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Mapping: You can use lambda functions with the map function to apply a function to all elements in a list.

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Summary
# Lambda functions are useful for short, one-off tasks where defining a full function is unnecessary.
# They help keep your code concise and readable when used appropriately.
# Commonly used in situations where a small function is required for a short period, such as sorting, filtering, and
# mapping.

# Extra exercises
# Exercise 1: Sorting by Length
# Given a list of strings, sort the list based on the length of each string using a lambda function.

words = ["banana", "apple", "cherry", "blueberry", "kiwi"]
words.sort(key=lambda word: len(word))
print(words)  # Output: ['kiwi', 'apple', 'banana', 'cherry', 'blueberry']

# Exercise 2: Filtering Even Numbers
# Use a lambda function with the filter function to filter out all even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Exercise 3: Mapping to Squares
# Use a lambda function with the map function to create a new list where each number is squared.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Exercise 4: Custom Sorting
# Sort a list of dictionaries based on a specific key using a lambda function.

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 72},
    {"name": "Charlie", "grade": 95},
    {"name": "David", "grade": 85}
]
students.sort(key=lambda student: student['grade'])
print(students)
# Output: [{'name': 'Bob', 'grade': 72}, {'name': 'David', 'grade': 85}, {'name': 'Alice', 'grade': 88}, {'name':
# 'Charlie', 'grade': 95}]

# Exercise 5: Sorting by Last Name
# Given a list of names, sort the list based on the last name using a lambda function.

names = ["John Doe", "Jane Smith", "Alice Johnson", "Charlie Brown"]
names.sort(key=lambda name: name.split()[-1])
print(names)  # Output: ['Charlie Brown', 'John Doe', 'Alice Johnson', 'Jane Smith']

# Exercise 6: Applying Discounts
# Given a list of prices, use a lambda function to apply a 10% discount to each price.

prices = [100, 200, 300, 400, 500]
discounted_prices = list(map(lambda price: price * 0.9, prices))
print(discounted_prices)  # Output: [90.0, 180.0, 270.0, 360.0, 450.0]

# Exercise 7: Combining Lists
# Use a lambda function with the map function to combine two lists element-wise by adding corresponding elements.

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
combined = list(map(lambda x, y: x + y, list1, list2))
print(combined)  # Output: [11, 22, 33, 44]

# Exercise 8: Filtering Strings
# Use a lambda function with the filter function to filter out strings that contain the letter 'a'.

strings = ["apple", "banana", "cherry", "date", "fig"]
no_a_strings = list(filter(lambda x: 'a' not in x, strings))
print(no_a_strings)  # Output: ['cherry', 'fig']

# Exercise 9: Complex Sorting
# Sort a list of tuples based on the second element, and if they are the same, sort by the first element.

data = [(2, 3), (1, 2), (4, 3), (2, 2), (3, 1)]
data.sort(key=lambda x: (x[0], x[1]))
print(data)  # Output: [(3, 1), (1, 2), (2, 2), (2, 3), (4, 3)]

# Exercise 10: Conditional Mapping
# Use a lambda function with the map function to replace negative numbers in a list with zero.

numbers = [-1, 2, -3, 4, -5]
non_negative = list(map(lambda x: x if x >= 0 else 0, numbers))
print(non_negative)  # Output: [0, 2, 0, 4, 0]
