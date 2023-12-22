# functionargument {There are four types of arguments that we can provide in a function}


# 1. Default Arguments {We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.}


def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)


name("Amy")

# 2. Keyword Arguments{We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.}


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)


name(mname="Peter", lname="Wesker", fname="Jade")

# 3. Variable length Arguments{Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.}


def name(*name):
    print("Hello,", name[0], name[1], name[2])


name("James", "Buchanan", "Barnes")

# 4.  Required Arguments{In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.}


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)


name("Peter", "Quill", "rish")


# 5.  return Statement{The return statement is used to return the value of the expression back to the calling function.}


def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname


print(name("James", "Buchanan", "Barnes"))
