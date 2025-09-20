# Python Inheritance
#  allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.
#
# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
#
# Example
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when
# creating the child class:
#
# Example
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass


# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
#
# Now the Student class has the same properties and methods as the Person class.
#
# Example
# Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
#
# We want to add the __init__() function to the child class (instead of the pass keyword).
#
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
#
# Example
# Add the __init__() function to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname):
#     #add properties etc.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
#
# Example
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are
# ready to add functionality in the __init__() function.
#
# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its
# parent:
#
# Example
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit
# the methods and properties from its parent.
#
# Add Properties
# Example
# Add a property called graduation_year to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduation_year = 2019


x = Student("Mike", "Olsen")


# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student
# objects. To do so, add another parameter in the __init__() function:
#
# Example
# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year


x = Student("Mike", "Olsen", 2019)


# Add Methods
# Example
# Add a method called welcome to the Student class:

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)


# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the
# parent method will be overridden.


class Animal:
    def __init__(self, legs, tail, eyes, ears):
        self.legs = legs
        self.tail = tail
        self.eyes = eyes
        self.ears = ears

    def allAttributesThere(self):
        print(self.legs, self.tail, self.eyes, self.ears)


class Dog(Animal):
    def __init__(self, legs, tail, eyes, ears):
        super().__init__(legs, tail, eyes, ears)
        self.a = "a"
        self.b = "a"


x = Dog(1, 2, 3, 4)
print(x.a)

x.allAttributesThere()


class Cat(Animal):
    def __init__(self, legs, tail, eyes, ears, e, f):
        super().__init__(legs, tail, eyes, ears)
        self.e = e
        self.f = f

    def allAttributesThere(self):
        print(self.legs, self.tail, self.eyes, self.ears, self.e, self.f)


x = Cat("a", "b", "c", "d", "e", "f")

x.allAttributesThere()


# Advanced Concepts in Python Inheritance

# 1. Multiple Inheritance
# Python allows a class to inherit from multiple parent classes. This is useful in scenarios where a class needs to
# combine functionalities from different sources.
#
# Example:

class Bird:
    def fly(self):
        print("I can fly!")


class Fish:
    def swim(self):
        print("I can swim!")


class Penguin(Bird, Fish):
    def walk(self):
        print("I can walk too!")


penguin = Penguin()
penguin.fly()
penguin.swim()
penguin.walk()


# Notes: Discuss the Method Resolution Order (MRO) to explain how Python determines which method to call when there are
# multiple parent classes.

# 2. Access Modifiers
# Python doesn’t have strict access modifiers like private, protected, and public in other languages, but it uses naming
# conventions:
#
# Public Attributes: Accessible everywhere (default behavior).
# Protected Attributes: Prefix with a single underscore _.
# Private Attributes: Prefix with double underscores __.
# Example:

class Vehicle:
    def __init__(self):
        self.public = "I am public!"
        self._protected = "I am protected!"
        self.__private = "I am private!"

    def get_private(self):
        return self.__private


car = Vehicle()
print(car.public)  # Accessible
print(car._protected)  # Accessible but discouraged
# print(car.__private)   # AttributeError
print(car.get_private())  # Access private using a method


# 3. Polymorphism
# Polymorphism allows the same method name to have different behaviors based on the class using it.
#
# Example:

class Bird:
    def sound(self):
        print("Chirp chirp")


class Dog:
    def sound(self):
        print("Woof woof")


def make_sound(animal):
    animal.sound()


bird = Bird()
dog = Dog()
make_sound(bird)
make_sound(dog)

# 4. Abstract Classes
# Use the abc module to create abstract classes. An abstract class can’t be instantiated and serves as a blueprint for
# child classes.
#
# Example:

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Woof woof")


class Cat(Animal):
    def sound(self):
        print("Meow meow")


dog = Dog()
cat = Cat()
dog.sound()
cat.sound()


# 5. Mixin Classes
# Mixin classes are used to add reusable functionality to classes without being a part of the main class hierarchy.
#
# Example:

class WalkMixin:
    def walk(self):
        print("I can walk!")


class FlyMixin:
    def fly(self):
        print("I can fly!")


class Human(WalkMixin):
    pass


class Bird(WalkMixin, FlyMixin):
    pass


human = Human()
bird = Bird()
human.walk()
bird.walk()
bird.fly()


# 6. Dynamic Attributes
# Teach how attributes can be added dynamically to objects and how to use the __dict__ attribute to view all properties
# of an object.
#
# Example:

class Animal:
    pass


dog = Animal()
dog.name = "Buddy"
dog.age = 5

print(dog.name)
print(dog.__dict__)  # View all dynamic attributes


# Exercises for Practice

# 1. Multiple Inheritance
# Create a class hierarchy where:
# Vehicle has a move() method.
# Flyable has a fly() method.
# Car inherits from Vehicle.
# FlyingCar inherits from both Car and Flyable.
class Vehicle:
    def move(self):
        print("I can move on the ground!")


class Flyable:
    def fly(self):
        print("I can fly!")


class Car(Vehicle):
    def drive(self):
        print("I can drive!")


class FlyingCar(Car, Flyable):
    def describe(self):
        print("I am a flying car!")


flying_car = FlyingCar()
flying_car.move()  # Inherited from Vehicle
flying_car.drive()  # Inherited from Car
flying_car.fly()  # Inherited from Flyable
flying_car.describe()


# 2. Polymorphism
# Create a function that takes an object and calls a method common to different classes (e.g., start() for Engine, Fan,
# Car).
class Engine:
    def start(self):
        print("Engine starting...")


class Fan:
    def start(self):
        print("Fan spinning...")


class Car:
    def start(self):
        print("Car engine roaring...")


def start_object(obj):
    obj.start()


engine = Engine()
fan = Fan()
car = Car()

start_object(engine)  # Output: Engine starting...
start_object(fan)  # Output: Fan spinning...
start_object(car)  # Output: Car engine roaring...

# 3. Abstract Classes
# Design an abstract class Shape with an abstract method area(). Implement it in Circle and Rectangle.
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415926 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(4, 7)

print(f"Circle area: {circle.area()}")  # Output: 78.5
print(f"Rectangle area: {rectangle.area()}")  # Output: 28


# 4. Custom Access
# Implement a class BankAccount with private attributes for balance and methods to deposit() and withdraw().
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid or insufficient funds.")

    def check_balance(self):
        return self.__balance


# Example usage
account = BankAccount(100)
account.deposit(50)  # Output: Deposited 50. New balance: 150
account.withdraw(30)  # Output: Withdrew 30. New balance: 120
print(account.check_balance())  # Output: 120
