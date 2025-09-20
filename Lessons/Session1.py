# Global Variable
x = "fun"


def myfunc1():
    print("Learning is " + x)
    print("farah")


myfunc1()

y = "fun"


def myfunc2():
    # Local Variable
    y = "fantastic"
    print("\nLearning is " + y)


myfunc1()

print("Learning is " + y)


# "global" keyword
def myfunc3():
    global z
    z = "awesome"


myfunc3()

print("\nLearning is " + z)

# Change global variable inside a function
w = "great"


def myfunc4():
    global w
    w = "fantastic"


myfunc4()

print("\nPython is " + w)

Listname = ["ListnameA", "ListnameB", "listnameC", "ListnameD"]
d, b, c, a = Listname
print(a)
# a = ListnameD, b = ListnameB, c = ListnameC, d = ListnameA
