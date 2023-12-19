# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable


a = input()
print("My Name is", a)

x = input("Enter firt number:")
y = input("Enter secound number:")
print(x+y)  # 12100 because this only take string
print(int(x) + int(y))  # 112
