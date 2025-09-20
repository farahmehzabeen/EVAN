# Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# Display a string literal with the print() function:
print("Hello")
print('hello')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline string
b = """qndwkjfnjkfn
qjwfnwkfjenf
qnjebwdhjw
"""
print(b)

b = '''qndwkjfnjkfn you
qjwfnwkfjenf
qnjebwdhjw
'''
print(b)


# Strings are Arrays. Like many other popular programming languages, strings in Python are arrays of bytes representing
# unicode characters. However, Python does not have a character data type, a single character is simply a string with a
# length of 1. Square brackets can be used to access elements of the string.
# Note: The first character has index 0.


# Get the character at position 1 (remember that the first character has the position 0):
c = "Hello, World!"
print("character in position 1: " + c[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# To get the length of a string, use the len() function.
print(len(c))

# To check if a certain phrase or character is present in a string, we can use the keyword "in".
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement; Print only if "free" is present:
if "free" in txt:
    print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword : "not in".
# Check if "expensive" is NOT present in the following text:
print("expensive" not in txt)

# Use it in an if statement; Print only if "expensive" is NOT present:
if "expensive" in txt:
    print("No, 'expensive' is NOT present.")