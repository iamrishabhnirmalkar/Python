# Conditional Statements
# >, <, >=, <=, ==, !=
# {In Python, indentation is used to define a block of code.}

# 1. if else
a = int(input("Enter Your age"))
print("Your age is:", a)

if (a > 18):
    print("You can drive")
else:
    print("You cannot drive")

# 2. elif

num = int(input("Enter the value of Num: "))
if (num < 0):
    print("Number is negative")
elif (num == 0):
    print("Number is zero")
else:
    print("Number is postive")


# 3.  nested

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
