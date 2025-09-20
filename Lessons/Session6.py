# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an
# exception if the value is not found.
# Syntax: string.find(value, start, end)
# Parameter Values & Description: value	--> Required. The value to search for
# start --> Optional. Where to start the search. Default is 0
# end --> Optional. Where to end the search. Default is to the end of the string

# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))

# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# The format() method returns the formatted string.
# Syntax: string.format(value1, value2...)
# Parameter Values & Description: value1, value2...	Required. One or more values that should be formatted and inserted
# in the string.
# The values are either a list of values separated by commas, a key=value list, or a combination of both.
# The values can be of any data type.
# The Placeholders: The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty
# placeholders {}.

# Using different placeholder values:
txt1 = "My name is {name}, I'm {age}".format(name="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 38)
txt3 = "My name is {}, I'm {}".format("John", 39)

print(txt3)


# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# Definition and Usage: The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1
# if the value is not found.
# Syntax: string.index(value, start, end)
# Parameter Values & Description: value	--> Required. The value to search for.
# start	--> Optional. Where to start the search. Default is 0
# end --> Optional. Where to end the search. Default is to the end of the string

# Examples
# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# print(txt.index("q"))

# Booleans represent one of two values: True or False. In programming you often need to know if an expression is True or
# False. You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:
# Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Most Values are True. Almost any value is evaluated to True if it has some sort of content. Any string is True,
# except empty strings. Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return True:
print(bool("abc"), bool(123), bool(["apple", "cherry", "banana"]))

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0,
# and the value None. And of course the value False evaluates to False.
# The following will return False:
print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))
