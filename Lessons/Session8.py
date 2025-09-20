# Python input()
# The input() function takes input from the user and returns it.
"""
# Example
name = input("Enter your name: ")
print(name)

# The syntax of input() function is: input([prompt])
# input() Parameters -->
# The input() function takes a single optional argument:
# prompt (Optional) - a string that is written to standard output (usually screen) without trailing newline

# input() Return Value -->
# The input() function reads a line from the input (usually from the user), converts the line into a string by removing
# the trailing newline, and returns it.
# If EOF is read, it raises an EOFError exception.

# Example 1: How input() works in Python?
# get input from user
inputString = input()
print('The inputted string is:', inputString)

# Example 2: Get input from user with a prompt
# get input from user
inputString = input('Enter a string:')
print('The inputted string is:', inputString)

# Python Basic Input and Output

# Python Output
# In Python, we can simply use the print() function to print output. For example,
print('Python is powerful.\t Python is fun!')
# Here, the print() function displays the string enclosed inside the single quotation.

# Syntax of print()
# In the above code, the print() function is taking a single parameter. However, the actual syntax of the print function
# accepts 5 parameters
# print(object= separator = end = file = flush =)
# Here, object - value(s) to be printed
# sep(optional) - allows us to separate multiple objects inside print().
# end(optional) - allows us to add specific values like new line "\n", tab "\t"
# file(optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush(optional) - boolean specifying if the output is flushed or buffered. Default: False

# Example 1: Python Print Statement
print('Good Morning!')
print('It is rainy today')
# In the above example, the print() statement only includes the object to be printed.
# Here, the value for end is not used. Hence, it takes the default value '\n'. So we get the output in two different
# lines.

# Example 2: Python print() with end Parameter
# print with end whitespace
print('Good Morning!', end=' ')
print('It is rainy today')
# Notice that we have included the end = ' ' after the end of the first print() statement.
# Hence, we get the output in a single line separated by space.

# Example 3: Python print() with sep parameter
print('New Year', 2023, 'See you soon!', sep='. ')
# In the above example, the print() statement includes multiple items separated by a comma.
# Notice that we have used the optional parameter sep = ". " inside the print() statement.
# Hence, the output includes items separated by "." not comma.

# Example: Print Python Variables and Literals
# We can also use the print() function to print Python variables. For example,
number = -10.6
name = "Programming"
# print literals
print(5)
# print variables
print(number)
print(name)

# Example: Print Concatenated Strings
# We can also join two strings together inside the print() statement. For example,
print('Programming is ' + 'awesome.')
# Here, the + operator joins two strings 'Programming is ' and 'awesome.' the print() function prints the joined string

# Output formatting
# Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format()
# method.For example,
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))
# Here, the curly braces {} are used as placeholders. We can specify the order in which they are printed by using
# numbers (tuple index).

# Python Input
# While programming, we might want to take the input from the user. In Python, we can use the input() function.
# Syntax of input() --> input(prompt)
# Here, prompt is the string we wish to display on the screen. It is optional.

# Example: Python User Input
# using input() to take user input
num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))
# In the above example, we have used the input() function to take input from the user and stored the user input in the
# num variable.

# It is important to note that the entered value is a string, not a number. So, type(num) returns <class 'str'>.
# To convert user input into a number we can use int() or float() functions as:

num = int(input('Enter a number: '))
print('Data type of num:', type(num))
# Here, the data type of the user input is converted from string to integer.
"""

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.
# Example --> If statement:
a = 33
b = 200
if b > a:
    print("b is greater than a")
# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater
# than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater
# than a".

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming
# languages often use curly-brackets for this purpose.

# Example --> If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
    print("b is greater than a")  # you will get an error

# Elif: The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# Example
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to
# screen that "a and b are equal".

# Else: The else keyword catches anything which isn't caught by the preceding conditions.
# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go
# to the else condition and print to screen that "a is greater than b".

# You can also have an else without the elif:
# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If: have only one statement to execute, you can put it on the same line as the if statement.
# Example --> One line if statement:
if a > b: print("a is greater than b")

# Short Hand If ... Else: If you have only one statement to execute, one for if, and one for else, you can put it all on
# the same line:
# Example --> One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")
# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:
# Example --> One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And: The and keyword is a logical operator, and is used to combine conditional statements:
# Example --> Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or: The or keyword is a logical operator, and is used to combine conditional statements:
# Example --> Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Not: The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# Example --> Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested If: You can have if statements inside if statements, this is called nested if statements.
# Example
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement: if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
# Example
a = 33
b = 200

if b > a:
    pass
