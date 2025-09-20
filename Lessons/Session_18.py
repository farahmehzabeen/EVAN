# Python Sets
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and
# Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, unindexed,and  do not allow duplicate values.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#
# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.
#
# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Example
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# Example
# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
# Example
# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.
# Example
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type:
# Example
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:
# Example
# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))
# From Python's perspective, sets are defined as objects with the data type 'set': <class 'set'>
# Example
# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
# Example
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove items and add new items.
#
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a
# particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the
# in keyword.
# Example
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Example
# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Example
# Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# Change Items: Once a set is created, you cannot change its items, but you can add new items.

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# Example
# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
# To add items from another set into the current set, use the update() method.
# Example
# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists,
# dictionaries etc.).
# Example
# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Example
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

# Example
# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure
# what item that gets removed.
# The return value of the pop() method is the removed item.
# Example
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Example
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Example
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)

# Loop Items
# You can loop through the set items by using a for loop:
# Example
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Union
# The union() method returns a new set with all items from both sets.
# It does not maintain the order when the set items are strings.
# Example
# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# You can use the | operator instead of the union() method, and you will get the same result.

# Example
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
# Example
# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators:
# Example
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
# Example
# Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
# Note: The | operator only allows you to join sets with sets, and not with other data types like you can with the
# union() method.

# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
# Example
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.

# Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# Example
# Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.
# Example
# Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the
# intersecton() method.
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of
# returning a new set.
# Example
# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
# Example
# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present
# in the other set.
# Example
# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set2.difference(set1)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
# Example
# Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the
# difference() method.
# The difference_update() method will also keep the items from the first set that are not in the other set, but it will
# change the original set instead of returning a new set.
# Example
# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# Example
# Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# Example
# Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the
# symmetric_difference() method.
# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set
# instead of returning a new set.
# Example
# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# Python has a set of built-in methods that you can use on sets.

# Method	        Shortcut	Description
# add()	 	                    Adds an element to the set

# Add an element to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
# Definition and Usage: The add() method adds an element to the set. If the element already exists, the add() method
# does not add the element.
# Syntax -> set.add(elmnt)
# Parameter -. elmnt; Description ->Required. The element to add to the set
# Example
# Try to add an element that already exists:
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)

# clear()	 	                Removes all the elements from the set

# Remove all elements from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
# Definition and Usage: The clear() method removes all elements in a set.
# Syntax -> set.clear()
# No parameters

# copy()	 	                Returns a copy of the set

# Copy the fruits set:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
# Definition and Usage: The copy() method copies the set.
# Syntax -> set.copy()
# No parameters

# difference()	        -	    Returns a set containing the difference between two or more sets

# Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
# Definition and Usage: The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
# As a shortcut, you can use the - operator instead, see example below.
# Syntax -> set.difference(set1, set2 ... etc.)
# Parameter	  Description
# set1	      Required. The set(s) to check for differences in.
# set2	      Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with a comma.

# # Shorter Syntax -> set - set1 - set2 .... etc.
# Parameter	  Description
# set1	      Required. The set(s) to check for differences in.
# set2	      Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with - (a minus operator).
# Example
# Use - as a shortcut instead of difference():
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
myset = a - b
print(myset)

# Example
# Join more than two sets:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a.difference(b, c)
print(myset)

# Example
# Join more than two sets with the - operator:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a - b - c
print(myset)

# Example
# Reverse the example on the top of this page. Return a set that contains the items that only exist in set y, and not in
# set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

# difference_update()	-=	    Removes the items in this set that are also included in another, specified set

# Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# Definition and Usage: The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, because the difference() method returns a
# new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original
# set.
# As a shortcut, you can use the -= operator instead, see example below.
# Syntax -> set.difference_update(set1, set2 ... etc.)
# Parameter	   Description
# set1	       Required. The set(s) to check for differences in.
# set2	       Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with a comma.

# Shorter Syntax
# set -= set1 | set2 ... etc.
# Parameter	    Description
# set1	        Required. The set(s) to check for differences in.
# set2	        Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with | (a pipe operator).

# Example
# Use -= as a shortcut instead of difference_update():
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a -= b
print(a)

# Example
# Join more than two sets:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a.difference_update(b, c)
print(a)

# Example
# Join more than two sets with the -= operator:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a -= b | c
print(a)

# discard()	 	                Remove the specified item

# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
# Definition and Usage: The discard() method removes the specified item from the set.
# This method is different from the remove() method, because the remove() method will raise an error if the specified
# item does not exist, and the discard() method will not.
# Syntax -> set.discard(value)
# Parameter	  Description
# value	      Required. The item to search for, and remove

# intersection()	    &	    Returns a set, that is the intersection of two other sets

# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# Definition and Usage: The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with
# more than two sets.
# As a shortcut, you can use the & operator instead, see example below.
# Syntax -> set.intersection(set1, set2 ... etc.)
# Parameter	   Description
# set1	       Required. The set to search for equal items in
# set2	       Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with a comma
# Shorter Syntax -. set & set1 & set2 ... etc.
# Parameter	   Description
# set1	       Required. The set to search for equal items in
# set2         Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with & (a and operator).

# Example
# Use & as a shortcut instead of intersection():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x & y
print(z)

# Example
# Join 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

# Example
# Join 3 sets with the & operator:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x & y & z
print(result)

# intersection_update()	&=	    Removes the items in this set that are not present in other, specified set(s)

# Remove the items that is not present in both x and y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# Definition and Usage
# The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison
# is done between more than two sets).
# The intersection_update() method is different from the intersection() method, because the intersection() method
# returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
# As a shortcut, you can use the &= operator instead, see example below.
# Syntax -> set.intersection_update(set1, set2 ... etc)
# Parameter	   Description
# set1	       Required. The set to search for equal items in
# set2	       Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with a comma
# Shorter Syntax -> set &= set1 & set2 ... etc.
# Parameter	   Description
# set1	       Required. The set to search for equal items in
# set2	       Optional. The other set to search for equal items in.
# You can compare as many sets you like. Separate the sets with & (a and operator).

# Example
# Use &= as a shortcut instead of intersection_update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x &= y
print(x)

# Example
# Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)

# Example
# Join 3 sets with the &= operator:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x &= y & z
print(result)

# isdisjoint()	 	            Returns whether two sets have a intersection or not

# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# Definition and Usage: The isdisjoint() method returns True if none of the items are present in both sets, otherwise it
# returns False.
# Syntax -> set.isdisjoint(set)
# Parameter	 Description
# set	     Required. The set to search for equal items in
# Example
# What if no items are present in both sets?
# Return False if one or more items are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

# issubset()	        <=	    Returns whether another set contains this set or not
#                    	<	    Returns whether all items in this set is present in other, specified set(s)

# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Definition and Usage: The issubset() method returns True if all items in the set exists in the specified set,
# otherwise it returns False.
# As a shortcut, you can use the <= operator instead, see example below.
# Syntax -> set.issubset(set1)
# Shorter Syntax -> set <= set1
# Parameter	  Description
# set1	      Required. The set to search for equal items in
# Example
# Use <= as a shortcut instead of issubset():
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x <= y
print(z)

# Example
# What if not all items are present in the specified set?
# Return False if not all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

# issuperset()	        >=	    Returns whether this set contains another set or not
#  	                    >	    Returns whether all items in other, specified set(s) is present in this set

# Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# Definition and Usage: The issuperset() method returns True if all items in the specified set exists in the original
# set, otherwise it returns False.
# As a shortcut, you can use the >= operator instead, see example below.
# Syntax -> set.issuperset(set)
# Shorter Syntax -> set >= set1
# Parameter	     Description
# set	         Required. The set to search for equal items in

# Example
# Use >= as a shortcut instead of issuperset():
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x >= y
print(z)

# Example
# What if not all items are present in the specified set?
# Return False if not all items in set y are present in set x:
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# pop()	 	                    Removes an element from the set

# Remove a random item from the set:
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# Definition and Usage: The pop() method removes a random item from the set.
# This method returns the removed item.
# Syntax -> set.pop()
# No parameter values.

# Example
# Return the removed element:
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)
# Note: The pop() method returns removed value.

# remove()	 	                Removes the specified element

# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# Definition and Usage: The remove() method removes the specified element from the set.
# This method is different from the discard() method, because the remove() method will raise an error if the specified
# item does not exist, and the discard() method will not.
# Syntax -> set.remove(item)
# Parameter	   Description
# item	       Required. The item to search for, and remove

# symmetric_difference() ^	    Returns a set with the symmetric differences of two sets

# Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Definition and Usage: The symmetric_difference() method returns a set that contains all items from both set, but not
# the items that are present in both sets.
# Meaning: The returned set contains a mix of items that are not present in both sets.
# As a shortcut, you can use the ^ operator instead, see example below.
# Syntax -> set.symmetric_difference(set1)
# Shorter Syntax -> set ^ set1
# Parameter	     Description
# set1	         Required. The set to check for matches in

# Example
# Use ^ as a shortcut instead of symmetric_difference():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x ^ y
print(z)

# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another

# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# Definition and Usage: The symmetric_difference_update() method updates the original set by removing items that are
# present in both sets, and inserting the other items.
# As a shortcut, you can use the ^= operator instead, see example below.
# Syntax -> set.symmetric_difference_update(set1)
# Shorter Syntax -> set ^= set1
# Parameter	    Description
# set1	        Required. The set to check for matches in

# Example
# Use ^= as a shortcut instead of symmetric_difference_update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x ^= y
print(x)

# union()	             |	    Return a set containing the union of sets

# Return a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# Definition and Usage: The union() method returns a set that contains all items from the original set, and all items
# from the specified set(s).
# You can specify as many sets you want, separated by commas.
# It does not have to be a set, it can be any iterable object.
# If an item is present in more than one set, the result will contain only one appearance of this item.
# As a shortcut, you can use the | operator instead, see example below.
# Syntax -> set.union(set1, set2...)
# Parameter	     Description
# set1	         Required. The iterable to unify with
# set2	         Optional. The other iterable to unify with.
# You can compare as many iterables as you like. Separate each iterable with a comma

# Shorter Syntax -> set | set1 | set2 ...
# Parameter	     Description
# set1	         Required. The iterable to unify with
# set2	         Optional. The other iterable to unify with.
# You can compare as many iterables as you like. Separate each iterable with | (a pipe operator).

# Example
# Use | as a shortcut instead of union():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)

# Example
# Unify more than 2 sets:
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)

# Example
# Unify 3 sets with the | operator:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x | y | z
print(result)

# update()	             |=	    Update the set with the union of this set and others

# Insert the items from set y into set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

# Definition and Usage: The update() method updates the current set, by adding items from another set (or any other
# iterable).
# If an item is present in both sets, only one appearance of this item will be present in the updated set.
# As a shortcut, you can use the |= operator instead, see example below.
# Syntax -> set.update(set1, set2 ...)
# Parameter	     Description
# set1	         Required. The iterable insert into the current set
# set2	         Optional. More iterables to insert into the current set.
# You can insert as many iterables as you like. Separate each iterable with a comma.

# Shorter Syntax -> set |= set1 | set2 ...
# Parameter	     Description
# set1	         Required. The set to insert into the current set.
# set2	         Optional. More sets to insert into the current set.
# You can insert as many sets you like. Separate the sets with | (pipe operator).

# Example
# Use |= as a shortcut instead of update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x |= y
print(x)

# Example
# Insert more than one set:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x.update(y, z)
print(x)

# Example
# Join more than one set with the |= operator:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x |= b | c
print(x)
