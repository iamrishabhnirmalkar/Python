# Function
# 1. Built-in functions {These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.}


# 2. User-defined functions

def calGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")


def isLesser(a, b):
    pass  # use when you give function but not to write now


a = 9
b = 8
isGreater(a, b)
calGmean(a, b)

c = 5
d = 9
isGreater(c, d)
calGmean(c, d)
