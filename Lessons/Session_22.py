# Python Classes/Objects
# Python is an object-oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# A class is a blueprint or template for creating objects. It defines a set of attributes (variables) and methods
# (functions) that the objects created from the class will have.

# Create a Class
# To create a class, use the keyword class:
# Example
# Create a class named MyClass, with a property named x:
class MyClass:
    x = 5


# Syntax
class ClassName:
    # Class attributes (optional)
    # Constructor method
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2

    # Class methods
    def method1(self):
        # Method body
        pass

    def method2(self, param):
        # Method body
        pass


# An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is
# created. Each object can have different attribute values, but they share the same methods defined by the class.

# Create Object
# Now we can use the class named MyClass to create objects:
# Example
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)


# Syntax
# object_name = ClassName(param1_value, param2_value)
#
# # Accessing object attributes and methods
# print(object_name.attribute1)  # Accessing attribute
# object_name.method1()  # Calling method


# Here's an example that demonstrates the concept of a class and an object.

# Defining a class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand1, model1, year1):
        self.brand = brand1
        self.model = model1
        self.year = year1

    # Method to describe the car
    def car_info(self):
        return f"This car is a {self.year} {self.brand} {self.model}."


# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

# Accessing attributes and methods
print(car1.car_info())  # Output: This car is a 2020 Toyota Corolla.
print(car2.car_info())  # Output: This car is a 2021 Honda Civic.


# In this example:
# Car is the class.
# car1 and car2 are objects (instances) of the Car class.
# __init__() is the constructor method that initializes the object's attributes.
# car_info() is a method that operates on the object's attributes.

# Key Points:
# Classes are templates, and objects are instances of classes.
# You can create multiple objects from a single class, each with different attribute values.
# Methods defined within the class operate on the object’s data (attributes).

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life
# applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when
# the object is being created:
# Example
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
# Example
# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)


# Example
# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The person is {self.name}({self.age})."


p1 = Person("John", 36)

print(p1)


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:
# Example
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs
# to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any
# function in the class:
# Example
# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)
        print(abc.age)


p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
# You can modify properties on objects like this:
# Example
# Set the age of p1 to 40:

p1.age = 40
p1.myfunc()

# Delete Object Properties
# You can delete properties on objects by using the del keyword:
# Example
# Delete the age property from the p1 object:
del p1.age

# Delete Objects
# You can delete objects by using the del keyword:
# Example
# Delete the p1 object:

del p1


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass
# statement to avoid getting an error.
# Example
# class Person:
#     pass
#

class S:

    def __init__(self, a, b, c, d):
        self.first_attribute = d
        self.second_attribute = c
        self.third_attribute = b
        self.fourth_attribute = a

    def concatenation(self):
        print(self.fourth_attribute + self.third_attribute)

    def addition(self):
        print(self.second_attribute + self.first_attribute)


s1 = S("a", "b", 4, 8)

s1.concatenation()
s1.addition()

s1.first_attribute = "b"
s1.second_attribute = "c"
s1.third_attribute = 205
s1.fourth_attribute = 215

s1.concatenation()
s1.addition()


# Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an
# argument student_name or student_class the function will print the student name and class.

# student_id = 345
# student_name = "John"
# student_class = "science"
#
#
# def student_data():
#     print(student_id)
#     if input() == "Student name":
#         print(student_name)
#     elif input() == "Student Class":
#         print(student_class)
#     else:
#         print("Invalid Input ):<")
#
#
# student_data()


# Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether
# they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in
# object class or not.

class Student:

    def __init__(self, name, age):
        self.a = name
        self.b = age


class Marks:
    pass


s1 = Student("John", 35)


# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said
# class and print the original and modified values of the said attributes.
class Student:
    def __init__(self, a, b):
        self.student_name = a
        self.marks = b


s2 = Student("John", 14)
print(s2.student_name)
print(s2.marks)


# Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class.
# Create a function to display all attributes and their values in the Student class.

class Student:
    # def __init__(self, a, b, c):
    #     self.student_id = a
    #     self.student_name = b
    #     self.student_class = c

    student_id = 12346270
    student_name = "John"
    student_class = "Math"

    def view():
        print(f'The attributes displayed are Student ID: {Student.student_id}, Student Name: {Student.student_name} '
              f'and Student Class: {Student.student_class}')


Student.view()


# Write a Python class named Student with two instances student1, student2 and assign values to the instances'
# attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
class Student:
    pass


s1 = Student()
