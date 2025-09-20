# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a
# class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean. You can create functions that returns a Boolean Value: Print the answer of a function:
def myFunction():
    return True


print(myFunction())


# You can execute code based on the Boolean answer of a function: Print "YES!" if the function returns True, otherwise
# print "NO!":
def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used
# to determine if an object is of a certain data type:
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

#  Operators are used to perform operations on variables and values.
# In the example below, we use the + operator to add together two values:
# Example
print(10 + 5)

# Python divides the operators in the following groups: Arithmetic operators, Assignment operators, Comparison operators
# Logical operators, Identity operators, Membership operators, Bitwise operators

# Arithmetic operators are used with numeric values to perform common mathematical operations:
# +	Addition
y = 20
print(x + y)
# Subtraction
print(x - y)
# Multiplication
print(x * y)
# Division
print(x / y)
# Modulus: the modulo operation returns the remainder or signed remainder of a division, after one number is divided by
# another. Given two positive numbers a and n, a modulo n is the remainder of the Euclidean division of a by n, where
# a is the dividend and n is the divisor.
# Dividend    Divisor
#    25    /     7    = 3 remainder 4
#    25    %     7    = 4
print(25 % 7)
# Exponentiation:
print(x ** y)
# Floor division: rounds the result down to the nearest whole number
print(x // y)

# Assignment operators are used to assign values to variables:
x = 5
x += 3  # x = x + 3
print(x)
x -= 3  # x = x - 3
print(x)  # 2
x *= 3  # x = x * 3
print(x)  # 15

x /= 3  # x = x / 3
print(x)  # 1.667

x %= 3  # x = x % 3
print(x)  # 2

x //= 3  # x = x // 3
print(x)  # 1

x **= 3  # x = x ** 3
print(x)  # 125
x = 5   # 0101
x &= 3  # 0011 # x = x & 3  Bitwise AND operation
#         0001
print(x)
x = 5   # 0101
x |= 3  # 0011  # x = x | 3  Bitwise OR operation
#         0111
print(x)
x = 5
x ^= 3  # x = x ^ 3   Exclusive OR operation
print(x)
x = 5
x >>= 3  # x = x >> 3  Right shift
print(x)
x = 5
x <<= 3  # x = x << 3  Left shift
print(x)

# Comparison operators are used to compare two values:
# ==	Equal
x = 5
y = 3
print(x == y)
# !=	Not equal
print(x != y)
# >	Greater than
print(x > y)
# <	Less than
print(x < y)
# >=	Greater than or equal to
print(x >= y)
# <=	Less than or equal to
print(x <= y)

# Logical operators are used to combine conditional statements:
# and 	Returns True if both statements are true
print(x < 5 and x < 10)
# or	Returns True if one of the statements is true
print(x < 5 or x < 4)
# not	Reverse the result, returns False if the result is true
print(not (x < 5 and x < 10))

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
# with the same memory location:
# is: Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # returns True because z is the same object as x
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)  # to demonstrate the difference between "is" and "==": this comparison returns True because x is equal
# to y
# is not: Returns True if both variables are not the same object
print(x is not z)  # returns False because z is the same object as x
print(x is not y)  # returns True because x is not the same object as y, even if they have the same content
print(x != y)  # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is
# equal to y

# Membership operators are used to test if a sequence is presented in an object:
# in --> Returns True if a sequence with the specified value is present in the object
print("banana" in x)  # # returns True because a sequence with the value "banana" is in the list
# not in --> Returns True if a sequence with the specified value is not present in the object
print("pineapple" not in x)  # returns True because a sequence with the value "pineapple" is not in the list

# Bitwise operators are used to compare (binary) numbers:
# & --> AND	Sets each bit to 1 if both bits are 1
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
"""
# |	--> OR	Sets each bit to 1 if one of two bits is 1
print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
"""
# ^	--> XOR	Sets each bit to 1 if only one of two bits is 1
print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
"""
# ~ --> NOT	Inverts all the bits
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
"""
# << --> Zero fill left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost 
bits fall off:
If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
"""
# >> --> Signed right shift: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost
# bits fall off
print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
 """

# Operator Precedence: describes the order in which operations are performed.
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)

# The precedence order is described below, starting with the highest precedence at the top:
# () --> Parentheses
print((6 + 3) - (6 + 3))
"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
# ** --> Exponentiation
print(100 - 3 ** 3)
"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""
# +x  -x  ~x --> Unary plus, unary minus, and bitwise NOT
print(100 + ~3)
"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""
# *  /  //  % --> Multiplication, division, floor division, and modulus
print(100 + 5 * 3)
"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""
# +  -	--> Addition and subtraction
print(100 - 5 * 3)
"""
Subtraction has a lower precedence than multiplication, and we need to calculate the multiplication first.
The calculation above reads 100 - 15 = 85
"""
# <<  >> --> Bitwise left and right shifts
print(8 >> 4 - 2)
"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
"""
# &	--> Bitwise AND
print(6 & 2 + 1)
"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2
More explanation:
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
"""
# ^	--> Bitwise XOR
print(6 ^ 2 + 1)
"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5
More explanation:
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
"""
# |	--> Bitwise OR
print(6 | 2 + 1)
"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7
More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
"""
# ==, !=, >, >=, <, <=, is, is not, in, not in --> Comparisons, identity, and membership operators
print(5 == 4 + 1)
"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""
# not --> Logical NOT
print(not 5 == 5)
"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""
# and --> AND
print(1 or 2 and 3)
"""
The and operator has a higher precedence than or, and we need to calculate the and expression first.
The calculation above reads: 1 or 3 = 1
"""
# or --> OR
print(4 or 5 + 10 or 8)
"""
The or operator has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads: 4 or 15 or 8 = 4
"""

# If two operators have the same precedence, the expression is evaluated from left to right.
# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)
