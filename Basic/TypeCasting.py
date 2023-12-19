# 1. Typecasting
# a = 1
# b = 2
# print(a+b)
# c = "1"
# d = 2
# print(c+d)
# 1.1 Explicit Conversion (Explicit Type casting in python) {The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion. It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .}

string = "15"
number = 7
# throws an error if the string is not a valid integer
string_number = int(string)
sum = number + string_number
print("The Sum of both the numbers is: ", sum)

# 1.2 implicit Conversion (Implicit Type casting in python){Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.}

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
