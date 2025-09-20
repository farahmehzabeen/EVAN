"""

x = 10
print(type(x))
age = 20
Age = 30
AGE = 40
print(AGE)

x = y = z = 5
print(x, y, z)

fruits = ["apple", "orange", "banana"]
x, y, z = fruits
print(x, y, z)

student_Information = ["John", "10", True]
name, age, is_new = student_Information
#John = Information
print("Student Name: " + name)
print("age:" + age)
print(is_new)

# Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"
# Create a variable named x and assign the value 50 to it.
x = 50

# Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x + y)
# Create a variable called z, assign x + y to it, and display the result.
z = x + y
print(z)
# Remove the illegal characters in the variable name:
my_first_name = "John"

# Write the correct syntax to assign the same value to all three variables in one code line.
w = x = y = z

#The following code example would print the data type of x, what data type would that be?
x = 5
print(type(x))

#The following code example would print the data type of x, what data type would that be?
x = "Hello World"
print(type(x))

#The following code example would print the data type of x, what data type would that be?
x = 20.5
print(type(x))

#The following code example would print the data type of x, what data type would that be?
x = ["apple", "banana", "cherry"]
print(type(x))

#The following code example would print the data type of x, what data type would that be?
x = ("apple", "banana", "cherry")
print(type(x))

#The following code example would print the data type of x, what data type would that be?
x = {"name" : "John", "age" : 36}
print(type(x))

#The following code example would print the data type of x, what data type would that be?
x = True
print(type(x))

"""
"""
# convert x into a floating point number/ integer/ complex.
x = 5
a = float(x)
print(a)
print(type(a))

x1 = 3.8
x1 = int(x1)
print(x1)
x2 = 5
x2 = complex(x2)
print(x2)
print(type(x2))
x3 = 6.4
x3 = complex(x3)
print(x3)
"""

# Integers:
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # what will z be?
print(x, y, z)

a = "Hello World"
print(len(a))
print(a[5])

if "great big" in a:
    print("ugkjykhgkgk")

if "great big" not in a:
    print("mmncnbcmb")

print("great big" in a)

for x in a:
    print(x)

b = "         My name is Evan        "
print(b[3:8])

d = "Today is a Sunday!"
print(d[-6:-2])

print(d.upper())
print(d.lower())

print(b.strip())
print(d.replace('a', 'w'))
print(d.replace('a', 'w', 2))

print(d.split('!'))

e = b + d
print(e)

a = 10
b = 20
c = a + b
print(c)

a = "tomorrow will be a better day!"
print(a.replace('r', 'z', 2))

print()

c = 5
b = "November {} is a great day!"
print(b.format(c))

d = "I went out for groceries and got {n1:.2f} apples, {type:.2f} lemons and {n2:.3f} strawberries."
# print(d.format(type, n1, n2))

e = "s\tt\trawberries"
print(e.center(30, "0"))
f = "I went out for groceries and wanted to get apples. I wanted 12 apples. But I forgot to bring any apples."
print(f.count("apple", 15, 30))
print(f.endswith("apples", 10, 40))
print(e.expandtabs(90))

print(f.find("o", 15, 25))

print(d.format(type=10.123, n1=15.34, n2=24.22345))

print(bool(f > d))


def funtion():
    return 1


print(funtion())

x = 10.32
print(isinstance(x, float))

print(x < 5 or x < 4)
print(not (x < 5 and x < 10))

x = 6
x |= 7
print(x)

# question = "What day is it?: "
# print(input(question), "\nbut it is sunday!", end=".", sep=":")

x = 60
y = 75
if x > y:
    print("a")
else:
    print("b")

a = 234
b = 456
if a > b:
    print("A is greater than B")
elif a == b:
    print("A and B are equal")
else:
    print("B is greater than A")

a = 25
b = 50
c = 25
d = 25
# Print "Hello World" if a is greater than b.
if a > b:
    print("Hello World")

# Print "Hello World" if a is not equal to b.
if a != b:
    print("Hello World")
# Print "Yes" if a is equal to b, otherwise print "No".
if a == b:
    print("yes")
else:
    print("no")
# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
# Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
    print("hello")
# Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
    print("hello")
# Print "YES" if 5 is larger than 2.
if 5 > 2:
    print("yes")

# Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
print("yes") if a == b else print("no")

# Use an if statement to print "YES" if either a or b is equal to c.
if a or b == c:
    print("yes")

"""
i = 10
while i <= 15:
    print(i)
    i -= 1
"""

# Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1
# Stop the loop if i is 3.
i = 10

# In the loop, when i is 3, jump directly to the next iteration.
while i > 0:
    # print(i)
    i -= 1
    if i == 3:
        continue
    print(i)

fruits = ["apple", "banana", "cherry", "pineapple", "strawberry", "blueberry"]
# Loop through the items in the fruits list.
for y in fruits:
    print(y)

for a in "strawberry":
    print(a)

# In the loop, when the item value is "banana", jump directly to the next item.
for x in fruits:
    if x == "banana": continue
    print(x)

# Use the range function to loop through a code set 6 times.
fruits = range(4)
for z in fruits:
    print("._.")

# Exit the loop when x is "banana".

thislist = ["a", "b", "c", "d"]
print(len(thislist), type(thislist), thislist)
mylist = list(("a", "b", "c"))
print(mylist)


def function(name, secondname):
    print("Hello World from")
    print(name + " and " + secondname)


function("Evan", "Farah")


def funcion2(*names):
    print(arrayname[7])


arrayname = ("a", "b", "c", "d", "e", "f", "g", "h")

funcion2()


def function3(*, x):
    print(x)


function3(x=3)


def function4(x, /, *, y):
    print(x, y)


function4(3, y=4)

letters = ["a", "b", "c"]
first_letter = letters[1]
print(first_letter)
print(len(letters))
letters[1] = "z"
print(letters[1])

for x in letters:
    print(x)

array = ["q", "w", "e", "t", "y", "w", "w"]
array2 = ["a", "b", "c"]
x = array.extend(array2)
print(array)
array3 = (1, 2, 3, 4)
y = array.append(array3)
print(array)
z = array.pop(4)
print(array)
w = array.insert(4, "strawberry")
print(array)
u = array.remove("t")
print(array)

b = array.pop()
h = array.insert(8, "k")
print(array)
t = array2.reverse()
print(array2)

array = ["kiwi", "strawberry", "banana", "apple", "orange", "tomato", "grape"]

"""def function6(e):
    return len(e)


print(array.sort(reverse=True, key=function6))"""
array[2:5] = ["blackcurrent", "cherry"]
print(array)
print(array[4:])

if 'orange' in array:
    print("yes")
elif "orange" not in array:
    print("no")
else:
    print("yes to strawberry")

array.insert(4, "pineapple")
print(array)

array.pop(4)
print(array)

array1 = ["kiwi", "strawberry", "banana", "apple"]
array2 = ("orange", "tomato", "grape")
array1.append(array2)
print(array1)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

array1.clear()
print(array1)

array3 = ["kiwi", "strawberry", "banana", "apple", "orange", "tomato", "grape"]
'''
for i in range(len(array3)):
    print(array3[i])

i = 0
while i in range(len(array)):
    print(array[i])
    i += 1
'''

# [print(x) for x in array]
fruits = ["apple", "banana", "cherry"]
array4 = []
for x in fruits:
    if "a" in x:
        array4.append(x)

print(array4)

newfruits = [x for x in fruits if "a" in x]
print(newfruits)

array6 = []
for x in array3:
    if "a" not in x:
        array6.append(x)
        print(array6)

array3 = ["kiwi", "strawberry", "banana", "apple", "orange", "tomato", "grape"]
array6 = []
for x in array3:
    if "a" in x:
        x = "blueberry"
    array6.append(x)

print(array6)

array6 = [x if "a" not in x else "blueberry" for x in array3]
print(array6)

fruits = ["apple", "banana", "cherry"]
# Use the correct syntax to print the number of items in the list.
list4 = ["a", "b", "c", "d", "e", "f", "g"]
print(len(list4))

# Print the second item in the fruits list.
print(fruits[1])
# Change the value from "apple" to "kiwi", in the fruits list.
# fruits.insert(0, "kiwi")
# print(fruits)

fruits1 = []
for x in fruits:
    if "p" in x:
        x = "kiwi"
        # fruits.append("kiwi")
        # fruits.pop(0)
    fruits1.append(x)

print(fruits1)

array7 = [x if "p" not in x else "kiwi" for x in fruits]
print(array7)

# Use the append method to add "orange" to the fruits list.
fruits.append("orange")
print(fruits)
# Use the insert method to add "lemon" as the second item in the fruits list.
fruits.insert(0, "lemon")
print(fruits)
# Use the remove method to remove "banana" from the fruits list.
fruits.remove("banana")
print(fruits)
# Use negative indexing to print the last item in the list.
print(fruits[-1])
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Use a range of indexes to print the third, fourth, and fifth item in the list.
array8 = [x.upper() for x in fruits]
print(array8)
array8.sort()
print(array8)
array8.sort(reverse=True)
print(array8)

print(fruits[3:6])


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True, key=myfunc)
print(thislist)

thistuple = (
    "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "cherry", "cherry", "cherry", "cherry", "cherry",
    "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry",
    "cherry",
    "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry",
    "cherry",
    "cherry", "cherry")
print(thistuple[-5:-2])

x = list(thistuple)
x.append("c")
x.append("v")
print(tuple(x))

x = list(thistuple)
# x.remove("apple")
x.pop(1)
y = tuple(x)
print(y)

(a, *b, c, d) = thistuple
print(a)
print(b)
print(c)
print(d)

for x in range(len(thistuple)):
    print(thistuple[x])

print(len(thistuple))
print(thistuple.count("cheery"))

set1 = {"apple", "banana", "cherry", "google", "microsoft", "apple"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set1.intersection_update(set2)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)

fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = y.difference(x)
# print(z)


set1 = {"apple", "banana", "cherry", "google", "microsoft", "apple"}
set2 = {"google", "microsoft", "apple"}
set3 = {"google", "microsoft", "apple", "cherry", "micra", "bluebird"}

set1 -= set2 | set3
print(set1)

fruits = {"apple", "banana", "cherry"}
# Check if "apple" is present in the fruits set.


# Use the add method to add "orange" to the fruits set.


# Use the correct method to add multiple items (more_fruits) to the fruits set.
more_fruits = ["orange", "mango", "grapes"]

# Use the remove method to remove "banana" from the fruits set.


# Use the discard method to remove "banana" from the fruits set.


# Exercise 1: Create a Set
# Description: Ask the user to input five elements and add them to a set. Then, print the set.

# user_input = input("Enter five numbers separated by spaces: ")
# user_list = user_input.split()
# user_set = set(user_list)
# print("Your set:", user_set)
#
# # Exercise 2: Add and Remove Elements
# # Description: Start with an empty set and ask the user to add three elements to it. Then, ask the user to remove one
# # element and print the set after each operation.
#
# my_set = set()
# # Add elements
# for _ in range(3):
#     element = input("Enter an element to add: ")
#     my_set.add(element)
#     print("Set after adding:", my_set)
#
# # Remove an element
# remove_element = input("Enter an element to remove: ")
# my_set.discard(remove_element)  # discard won't cause an error if the element doesn't exist
# print("Set after removing:", my_set)
#
# # Exercise 3: Set Operations
# # Description: Create two sets with numbers and demonstrate set operations like union, intersection, and difference.
# # Ask the user to choose an operation to perform.
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# print("Set 1:", set1)
# print("Set 2:", set2)
#
# operation = input("Choose an operation (union, intersection, difference): ")
#
# if operation == "union":
#     print("Union of sets:", set1 | set2)
# elif operation == "intersection":
#     print("Intersection of sets:", set1 & set2)
# elif operation == "difference":
#     print("Difference of sets (Set1 - Set2):", set1 - set2)
# else:
#     print("Invalid operation")
#
# # Exercise 4: Check for Membership
# # Description: Create a set with some pre-defined values. Ask the user to guess an element, and tell them if their
# guess
# # is in the set.
#
# fruits = {"apple", "banana", "cherry", "date"}
# guess = input("Guess a fruit: ")
#
# if guess in fruits:
#     print("Your guess is in the set!")
# else:
#     print("Sorry, your guess is not in the set.")

set1 = {}
set2 = {"google", "microsoft", "apple"}
set3 = {"google", "microsoft", "apple", "cherry", "micra", "bluebird"}

# set3.update(set2)
# print(set3)
#
# set4 = set2.symmetric_difference(set3)
# print(set4)

a = {"apple", "banana", "cherry", "google", "microsoft", "micra", "bluebird"}
# myset = a.difference(b, c)
# print(myset)


dict5 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": {"red", "white", "blue"}
}

print(type(dict5["colors"]))

dict7 = dict(brand="Ford", electric=False, year=1964, colors={"red", "white", "blue"})
print(dict7)

z = dict7.items()
print(z)

x = dict7.get("colors")
print(x)

x = dict7.keys()
y = dict7.values()
print(x)
print(y)

dict7["gas"] = "No"

print(dict7)
x = dict7.keys()
print(x)

dict7["colors"] = ("blue", "black", "red")

print(dict7)

x = dict7.items()
print(x)

if "oil" in dict7:
    print("2 + 2 = -5")

for x, y in dict7.items():
    print(x, y)

del dict7["electric"]
print(dict7)

dict7.clear()
print(dict7)

# Exercise 1: Creating and Accessing a Dictionary
# Create a dictionary named student with the following key-value pairs:
# "name": "Alice"
# "age": 12
# "grade": "7th"
# "subjects": ["Math", "Science", "English"]
# Print the value associated with the key "name".

student = {
    "name": "Alice",
    "age": "12",
    "grade": "7th",
    "subjects": ["Math", "Science", "English"]
}

x = student["name"]
print(x)

student["hobbies"] = ["reading", "swimming"]

print(student)

# Exercise 2: Modifying a Dictionary
# Using the student dictionary from Exercise 1, change the value of the "age" key to 13.
# Add a new key-value pair to the dictionary: "hobbies": ["reading", "swimming"].
# Print the updated dictionary.


# Exercise 3: Checking for Keys
# Check if the key "grade" exists in the student dictionary. If it does, print "Grade exists in the dictionary". If not,
# print "Grade does not exist in the dictionary".

if "grade" in student:
    print("Grade exists in the dictionary")
else:
    print("Grade does not exist in dictionary")

# Exercise 4: Removing Items
# Remove the "hobbies" key from the student dictionary using the pop() method.
# Print the updated dictionary.

student.pop("hobbies")
print(student)

# Exercise 5: Looping Through a Dictionary
# Loop through the keys of the student dictionary and print each key.
# Loop through the values of the dictionary and print each value.

for x in student:
    print(x)

for x in student:
    print(student.values())

# Exercise 6: Copying a Dictionary
# Make a copy of the student dictionary using the copy() method and name it student_copy.
# Print the copied dictionary.

student_copy = student.copy()
print(student_copy)

# Exercise 7: Using Dictionary Methods
# Create a new dictionary named grades using the fromkeys() method with the keys "Math", "Science", and "English", all
# having the value 0.
# Print the grades dictionary.

grades = dict
print(grades)

# Exercise 8: Updating a Dictionary
# Update the grades dictionary with the following key-value pairs:
# "Math": 95
# "Science": 88
# "English": 92
# Print the updated dictionary.

grades.update({"Math": 95, "Science": 88, "English": 92})
print(grades)

# Exercise 9: Using the setdefault() Method
# Use the setdefault() method to check if the key "history" exists in the grades dictionary. If it doesn't, add
# "history" with the value 80.
# Print the updated dictionary.

grades.setdefault("History", 80)

print(grades)

# Exercise 10: Combining Dictionaries
# Create two dictionaries:
# student_info with keys "name": "Bob", "age": 14
# student_scores with keys "math": 85, "science": 90
# Combine the two dictionaries into a new dictionary named student_combined using the update() method.
# Print the combined dictionary.

student_info = {
    "name": "Bob",
    "age": "14"
}

student_scores = {
    "math": 85,
    "science": 90
}

student_info.update(student_scores)
print(student_info)


# x = lambda a, b, c: a * b * c
# print(x(9, 2, 6))

def function(n):
    return lambda a: a * n


doubled = function(2)
tripled = function(3)
quarduple = function(4)

print(doubled(5))
print(tripled(5))
print(quarduple(5))

points = [(1, 2), (3, 1), (5, -1)]
points.sort(key=lambda points: points[1], reverse=True)
print(points)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
square_numbers = map(lambda x: x ** 3, numbers)
print(list(square_numbers))

# Exercise 1: Sorting by Length
# Given a list of strings, sort the list based on the length of each string using a lambda function.

words = ["banana", "apple", "cherry", "blueberry", "kiwi"]
words.sort(key=lambda x: len(x))
print(words)

# Exercise 2: Filtering Odd Numbers
# Use a lambda function with the filter function to filter out all odd numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(list(odd_numbers))

# Exercise 3: Mapping to Squares
# Use a lambda function with the map function to create a new list where each number is squared.


# Exercise 4: Custom Sorting
# Sort a list of dictionaries based on a specific key using a lambda function.

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 72},
    {"name": "Charlie", "grade": 95},
    {"name": "David", "grade": 85}
]

students.sort(key=lambda x: x['grade'], reverse=True)
print(students)
students.sort(key=lambda x: len(x['name']))
print(students)

# Exercise 5: Sorting by Last Name
# Given a list of names, sort the list based on the last name using a lambda function.


# Exercise 6: Applying Discounts
# Given a list of prices, use a lambda function to apply a 75% discount to each price.

prices = [100, 200, 300, 400, 500]
discount = map(lambda prices: prices * 0.25, prices)
print(list(discount))

# Exercise 7: Combining Lists
# Use a lambda function with the map function to combine two lists element-wise by adding corresponding elements.

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
list3 = map(lambda list1, list2: list1 * list2, list1, list2)
print(list(list3))

# Exercise 8: Filtering Strings
# Use a lambda function with the filter function to filter out strings that contain the letter 'o'.

cars = ["Ford", "Volvo", "BMW"]
a = filter(lambda cars: "o" in cars, cars)
print(list(a))

# Exercise 9: Complex Sorting
# Sort a list of tuples based on the second element, and if they are the same, sort by the first element.

data = [(2, 3), (1, 2), (4, 3), (2, 2), (3, 1)]
data.sort(key=lambda x: (x[0], x[1]))
print(data)

# Exercise 10: Conditional Mapping
# Use a lambda function with the map function to replace non-negative numbers in a list with zero.

numbers = [-1, 2, -3, 4, -5]
negative = map(lambda numbers: numbers if numbers < 0 else 0, numbers)
print(list(negative))


# You have two sets of ingredients:
#
# recipe1 = {"sugar", "flour", "butter", "milk", "eggs"}
# recipe2 = {"sugar", "flour", "butter", "chocolate", "vanilla"}
# Write a function unique_ingredients(recipe1, recipe2) that takes two sets as input and returns a new set containing
# the ingredients that are unique to each recipe (i.e., ingredients that are in either recipe1 or recipe2 but not in
# both).
#
# Print the result of calling unique_ingredients(recipe1, recipe2).
def unique_ingredients(recipe1, recipe2):
    # Use the symmetric difference operator to find unique ingredients
    return recipe1 ^ recipe2


# Given sets of ingredients for two recipes
recipe1 = {"sugar", "flour", "butter", "milk", "eggs"}
recipe2 = {"sugar", "flour", "butter", "chocolate", "vanilla"}

# Call the function and print the result
result = unique_ingredients(recipe1, recipe2)
print(result)


# You have two lists of numbers:
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Write a function common_elements(list1, list2) that takes two lists as input and returns a new list containing the
# elements that are common in both lists.
#
# Print the result of calling common_elements(list1, list2).
def common_elements(list1, list2):
    # Use a list comprehension to find common elements
    return [element for element in list1 if element in list2]


# Given lists of numbers
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Call the function and print the result
result = common_elements(list1, list2)
print(result)


# You have two arrays of words:
#
# array1 = ["apple", "banana", "cherry", "date"]
# array2 = ["banana", "date", "elderberry", "fig"]
# Write a function unique_words(array1, array2) that takes two arrays as input and returns a new list containing the
# words that are unique to each array (words that appear in either array1 or array2, but not in both).
#
# Print the result of calling unique_words(array1, array2).
def unique_words(array1, array2):
    # Use set operations to find unique elements in either array1 or array2
    unique_set = set(array1) ^ set(array2)
    # Convert the set back to a list
    return list(unique_set)


# Given arrays of words
array1 = ["apple", "banana", "cherry", "date"]
array2 = ["banana", "date", "elderberry", "fig"]

# Call the function and print the result
result = unique_words(array1, array2)
print(result)


# You have two lists of numbers:
#
# list1 = [1, 2, 2, 3, 4]
# list2 = [3, 4, 4, 5, 6]
# Write a function merge_and_remove_duplicates(list1, list2) that takes two lists as input and returns a new list that
# contains all the elements from both lists but with no duplicates.
#
# Print the result of calling merge_and_remove_duplicates(list1, list2).
def merge_and_remove_duplicates(list1, list2):
    # Merge the two lists and convert them to a set to remove duplicates
    merged_set = set(list1 + list2)
    # Convert the set back to a sorted list
    return list(merged_set)


# Given lists of numbers
list1 = [1, 2, 2, 3, 4]
list2 = [3, 4, 4, 5, 6]

# Call the function and print the result
result = merge_and_remove_duplicates(list1, list2)
print(result)

cars = ["Ford", "Volvo", "BMW", "Volvo"]
cars.remove("Volvo")
print(cars)


class dsf:
    def __init__(self, one, two, three, four):
        self.fhidlgsu = one
        self.knjjbkbjj = two
        self.gsfddhsgd = three
        self.fgdsgdfhf = four

    def sort(self, ):
        pass


p1 = dsf(1, 2, 3, 4)

p1.sort()

print(p1.fhidlgsu)


# class Person(object):
#
#     def get_name(self):
#
#         self.name = input("what is your name?")
#         ans = input("your name is %s right?" % self.name)
#
#         while ans == "no":
#             name = input("sorry about that, what is your name then?")
#             ans = "yes"
#         else:
#             print("nice to have you %s !!" % self.name)
#
#
# bob = Person()
# bob.get_name()


class S:

    def __init__(self, a, b, c, d):
        self.first_attribute = d
        self.second_attribute = c
        self.third_attribute = b
        self.fourth_attribute = a

    def concatenation(self):
        print(a)
        print(b)

    def addition(self):
        print(c)
        print(d)


s1 = S("a", "b", 4, 8)

s1.concatenation()
s1.addition()


# 1. Multiple Inheritance
# Create a class hierarchy where:
# Vehicle has a move() method.
# Flyable has a fly() method.
# Car inherits from Vehicle.
# FlyingCar inherits from both Car and Flyable.

class Vehicle:
    def move(self):
        print("I move!")


class Flyable:
    def fly(self):
        print("I fly!")


class Car(Vehicle):
    print("I'm able to scrape the ground below me!")


class FlyingCar(Vehicle, Flyable):
    print("qwhewi")


car = Car()
car.move()
car1 = FlyingCar()
car1.fly()


# 2. Polymorphism
# Create a function that takes an object and calls a method common to different classes (e.g., start() for Engine, Fan,
# Car).

class Engine:
    def start(self):
        print("Okok im starting")


class Fan:
    def start(self):
        print("okok im gonna go in circles")


class Car:
    def start(self):
        print("okok im caring")


def FunctionThatTakesAnObjectAndCallsAMethodCommonToDifferentClassesExSEngineFanAndCar(machine):
    machine.start()


engine = Engine()
FunctionThatTakesAnObjectAndCallsAMethodCommonToDifferentClassesExSEngineFanAndCar(engine)
# pls work plsplsplsplsplsplsplsplsplsplspls

# 3. Abstract Classes
# Design an abstract class Shape with an abstract method area(). Implement it in Circle and Rectangle.

# Exercise
# Define a function that calculates the square of a number using a local variable.
# Try to print the local variable outside the function. Observe the error.
def dfodsfvdfcvdfdfg():
    a = 37
    print(a)

print(dfodsfvdfcvdfdfg())

# Exercise
# Create an outer function that defines a local variable and an inner function that modifies it (use nonlocal).

def outer():
    x = 50
    def inner():
        nonlocal x
        x = 52

    inner()
    print(x)

outer()
print(x)


# Exercise
# Declare a global variable and use it in multiple functions.
# Experiment by reassigning it inside a function and observe what happens.
global_variable = "e"

def function1():
    global_variable = "a"
    print(global_variable)

def function2():
    print(global_variable)

function2()
function1()


# Exercise
x = 10  # Global variable

def local_example():
    global x
    x = 20  # Local variable
    print(f"Local x: {x}")

local_example()
print(f"Global x: {x}")
# Modify the code above to use global x inside the function. Observe how the global variable changes.


# Exercise
# Create a global list and a function to append items to it using global.
list = []

def function(thing):
    global list
    list.append(thing)
    print(thing)

function("testitem1")
function("testitem2")

print(list)
# Exercise
# Create a nested function structure where the inner function modifies a variable in the outer function using nonlocal.

def outer():
    kgmggjjgjgg = "100"

    def inner():
        nonlocal kgmggjjgjgg
        kgmggjjgjgg = "200"

    inner()
    print(kgmggjjgjgg)

outer()
print(kgmggjjgjgg)

global_var = "I'm global"

def access_global():
    print(global_var)  # Accessing global_var inside the function

access_global()
print(global_var)  # Accessing global_var outside the function

x = 100  # Global variable

def display_global():
    print(f"Global x: {x}")

def modify_global():
    global x  # Refers to the global variable
    x = 200
    print(f"Modified global x inside function: {x}")

display_global()
modify_global()
print(f"Global x after modification: {x}")

#def outer_function():
    #x = 5
    #def inner_function():
        #x += 1  # This will raise an error because x is not accessible here
    #inner_function()

#outer_function()
