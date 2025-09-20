# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

# Merge variable e with variable f into variable g:
e = "Hello"
f = "World"
g = e + f
print(g)

# To add a space between them, add a " ":
h = e + " " + f
print(h)

# cannot combine strings and numbers like this
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}
# are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

###### String Methods ########

# The capitalize() method returns a string where the first character is upper case, and the rest are converted to
# lower case.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

txt = "python is FUN!"
x = txt.capitalize()
print(x)

txt = "36 is my age."
x = txt.capitalize()
print(x)

# The lower() method returns a string where all characters are lower case; Symbols and Numbers are ignored.
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it
# will convert more characters into lower case, and will find more matches when comparing two strings and both are
# converted using the casefold() method.
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# The center() method will center align the string, using a specified character (space is default) as the fill character
# Syntax: string.center(length, character)
# Parameter Descriptions: length --> Required. The length of the returned string; character	--> Optional.
# The character to fill the missing space on each side. Default is " " (space)
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)

# Using the letter "O" as the padding character:
txt = "banana"
x = txt.center(20, "O")
print(x)

# The count() method returns the number of times a specified value appears in the string.
# Syntax: string.count(value, start, end)
# Parameter Values & Description: value --> Required. A String. The string to value to search for
# start --> Optional. An Integer. The position to start the search. Default is 0
# end --> Optional. An Integer. The position to end the search. Default is the end of the string
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# The endswith() method returns True if the string ends with the specified value, otherwise False.
# Syntax: string.endswith(value, start, end)
# Parameter Values & Description: value	--> Required. The value to check if the string ends with
# start	--> Optional. An Integer specifying at which position to start the search
# end --> Optional. An Integer specifying at which position to end the search
# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# The expandtabs() method sets the tab size to the specified number of whitespaces.
# Syntax: string.expandtabs(tabsize)
# Parameter Values & Description: tabsize --> Optional. A number specifying the tabsize. Default tabsize is 8
# See the result using different tab sizes:
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))