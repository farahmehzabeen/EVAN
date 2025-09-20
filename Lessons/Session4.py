c = "Hello, World!"

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
# c = "Hello, World!"
print(c[2:5])

# Slice From the Start. By leaving out the start index, the range will start at the first character.
# Get the characters from the start to position 5 (not included):
print(c[:5])

# Slice To the End By leaving out the end index, the range will go to the end.
# Get the characters from position 2, and all the way to the end:
print(c[2:])

# Negative Indexing. Use negative indexes to start the slice from the end of the string.
# Get the characters: From: "o" in "World!" (position -5); To, but not included: "d" in "World!" (position -2):
print(c[-5:-2])

# built-in methods that you can use on strings.
# Upper case: The upper() method returns the string in upper case.
print(c.upper())

# Lower case: The lower() method returns the string in lower case.
print(c.lower())

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
d = " Hello, World! "
print(d.strip())  # returns "Hello, World!"

# The replace() method replaces a string with another string:
print(c.replace("l", "J"))

# The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:
print(c.split(","))  # returns ['Hello', ' World!']