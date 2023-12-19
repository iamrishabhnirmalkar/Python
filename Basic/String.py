# # String {In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.}

# name = "rishabh"
# friend = 'Harry'

# print("Hello " + name)  # Hello rishabh

# apple = "he said , \"I want aapple\""
# print(apple)  # he said , "I want aapple"

# # 1. Accessing Characters of a String
# # In Python, string is like an array of characters

# print(name[0])  # r
# # print(name[8])  # IndexError: string index out of range


# # 2.Looping through the string

# for characters in name:
#     print(characters)

# for characters01 in apple:
#     print(characters01)


# 3. Length of a String
# 4. String as an array
names = "rishabh, rsihu"
print(len(names))  # 14
print(names[0:6])  # rishab

# 5. Slicing

fruit = "Mango"
print(len(fruit))  # 5
# print(fruit[1:4])
# print(fruit[1:])
# print(fruit[:5])

print(fruit[:len(fruit)-3])  # Ma { use len(fruit) so it value is 5-3=2}
print(fruit[0:-5])  # not print
print(fruit[-3:-1])  # ng
print(fruit[0:len(fruit)-1])

nm = "harry"
print(nm[-4:-2])  # ar
