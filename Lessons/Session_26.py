# What is Scope?
# Scope defines where a variable is accessible within a program. Variables can either have:
#
# Local Scope: Defined inside a function and accessible only within it.
# Global Scope: Defined outside all functions and accessible throughout the program.

# Example
def greet():
    message = "Hello, world!"  # Local variable
    print(message)

greet()
# print(message)  # This will raise an error because 'message' is not accessible here.

# Exercise
# Define a function that calculates the square of a number using a local variable.
# Try to print the local variable outside the function. Observe the error.
def calculate_square(num):
    square = num ** 2  # Local variable
    print(f"The square of {num} is {square}")

calculate_square(5)

# Trying to print the local variable outside the function
# print(square)  # Uncommenting this line will raise a NameError: 'square' is not defined


# Function Inside a Function
# Variables in the local scope of a function can be accessed by inner functions.
#
# Example
def outer_function():
    outer_var = "I'm in the outer function"

    def inner_function():
        print(outer_var)  # Accessing outer_var inside the inner function

    inner_function()


outer_function()

# Exercise
# Create an outer function that defines a local variable and an inner function that modifies it (use nonlocal).
def outer_function():
    message = "Outer"  # Local variable in the outer function

    def inner_function():
        nonlocal message  # Modifies the variable in the enclosing scope
        message = "Modified by Inner Function"

    inner_function()
    print(message)

outer_function()

# Global Scope
# Variables created outside any function are global. They can be accessed inside or outside any function.
# Example

global_var = "I'm global"

def access_global():
    print(global_var)  # Accessing global_var inside the function

access_global()
print(global_var)  # Accessing global_var outside the function

# Exercise
# Declare a global variable and use it in multiple functions.
# Experiment by reassigning it inside a function and observe what happens.
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

# Naming Conflicts Between Local and Global Variables
# If you use the same variable name inside and outside a function, Python treats them as separate variables.
#
# Example

x = 10  # Global variable

def local_example():
    x = 20  # Local variable
    print(f"Local x: {x}")

local_example()
print(f"Global x: {x}")

# Exercise
# Modify the code above to use global x inside the function. Observe how the global variable changes.
x = 300  # Global variable

def use_global_variable():
    global x
    x = 500  # Modifying the global variable
    print(f"x inside function: {x}")

use_global_variable()
print(f"x outside function: {x}")  # Prints the updated value

# Using the global Keyword
# The global keyword allows a local variable to modify a global variable.
# Example

counter = 0

def increment():
    global counter  # Declares that we're modifying the global variable
    counter += 1

increment()
increment()
print(counter)  # Should print 1

# Exercise
# Create a global list and a function to append items to it using global.
global_list = []  # Global list

def append_to_global(item):
    global global_list
    global_list.append(item)
    print(f"Item '{item}' added to global list.")

append_to_global("apple")
append_to_global("banana")
print(f"Global list: {global_list}")

# The nonlocal Keyword
# The nonlocal keyword allows modification of a variable in the nearest enclosing scope that is not global.
#
# Example

def outer_function():
    value = "Outer"

    def inner_function():
        nonlocal value  # Refers to 'value' in the outer function
        value = "Inner"

    inner_function()
    print(value)

outer_function()  # Should print "Inner"

# Exercise
# Create a nested function structure where the inner function modifies a variable in the outer function using nonlocal.
def outer_function():
    counter = 0  # Local variable in the outer function

    def increment():
        nonlocal counter  # Refers to the outer function's variable
        counter += 1
        print(f"Counter inside inner function: {counter}")

    for _ in range(5):
        increment()

    print(f"Final counter value: {counter}")

outer_function()


#
# Local Scope: A key to a room in a house (only works in that room).
# Global Scope: A master key to all rooms in the house.
# nonlocal: Borrowing the room key from the hallway.
#



# The error in your code occurs because the x variable in the inner_function is considered local by default when you
# attempt to modify it. However, the inner_function needs to access the x variable from the enclosing scope (outer
# function). To fix this, use the nonlocal keyword to explicitly refer to the x variable in the outer_function.
# Corrected version:
def outer_function():
    x = 5  # Variable in the outer function scope

    def inner_function():
        nonlocal x  # Access the variable from the outer function
        x += 1  # Modify the variable

    inner_function()
    print(f"Value of x after inner_function: {x}")

outer_function()

# Explanation:
# nonlocal x: This tells Python to use the x variable from the nearest enclosing scope (in this case, the
# outer_function), rather than treating it as a local variable inside inner_function.
# Without nonlocal, Python assumes you're trying to define a new local variable x in inner_function, which leads to the
# error since x += 1 tries to read an uninitialized local variable.
