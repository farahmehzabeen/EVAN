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
x = 5

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("x is not above 10!!")

# The pass Statement: if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
# Example
a = 33
b = 200

if b > a:
    pass