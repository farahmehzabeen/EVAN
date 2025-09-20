# Loop Through a List: You can loop through the list items by using a for loop:
# Example
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers: You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
# Example
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# The iterable created in the example above is [0, 1, 2].

# Using a While Loop: You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items
# by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
# Example
# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# Example
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension: offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax => newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# Condition: The condition is like a filter that only accepts the items that valuate to True.
# Example
# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all
# fruits except "apple".

# The condition is optional and can be omitted:
# Example
# With no if statement:
newlist = [x for x in fruits]
print(newlist)

# Iterable: The iterable can be any iterable object, like a list, tuple, set etc.
# Example
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

# Same example, but with a condition:
# Example
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression: The expression is the current item in the iteration, but it is also the outcome, which you can manipulate
# before it ends up like a list item in the new list:
# Example
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

# You can set the outcome to whatever you like:
# Example
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Example
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Example
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Example
# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending: To sort descending, use the keyword argument reverse = True:
# Example
# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Example
# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Customize Sort Function: You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
# Example
# Sort the list based on how close the number is to 50:
def myfunc(n):
    return n - 50


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case
# letters:
# Example
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list. So if you want a case-insensitive sort
# function, use str.lower as a key function:
# Example
# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order: What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
# Example
# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes
# made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().
# Example
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
# Example
# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists: There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
# Example
# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
# Example
# Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
# Example
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# index() method
# Example
# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

# Definition and Usage: The index() method returns the position at the first occurrence of the specified value.
# Syntax --> list.index(elmnt)
# Parameter: elmnt; Description: Required. Any type (string, number, list, etc.). The element to search for

# More Examples
# What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
# Note: The index() method only returns the first occurrence of the value.

# insert() method
# Example
# Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

# Definition and Usage: The insert() method inserts the specified value at the specified position.
# Syntax --> list.insert(pos, elmnt)
# Parameter: pos;	Description: Required. A number specifying in which position to insert the value
# Parameter: elmnt;	Description: Required. An element of any type (string, number, object etc.)

# pop() method
# Example
# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
# Definition and Usage
# The pop() method removes the element at the specified position.
# Syntax --> list.pop(pos)
# Parameter: pos;	Description: Optional. A number specifying the position of the element you want to remove, default
# value is -1, which returns the last item

# Example
# Return the removed element:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
# Note: The pop() method returns removed value.

# remove() method
# Example
# Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

# Definition and Usage
# The remove() method removes the first occurrence of the element with the specified value.
# Syntax --> list.remove(elmnt)
# Parameter: elmnt;	Description:	Required. Any type (string, number, list etc.) The element you want to remove

# reverse() method
# Example
# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
# Definition and Usage
# The reverse() method reverses the sorting order of the elements.
# Syntax --> list.reverse(); No parameters

# The built-in function reversed() returns a reversed iterator object.

# sort() method
# Example
# Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

# Definition and Usage
# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax --> list.sort(reverse=True|False, key=myFunc)
# Parameter: reverse;	Description: Optional. reverse=True will sort the list descending. Default is reverse=False
# Parameter: key; Description: Optional. A function to specify the sorting criteria(s)

# Example
# Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

# Example
# Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

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

# Example
# Sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
