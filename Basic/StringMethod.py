# StringMethod {Python provides a set of built-in methods that we can use to alter and modify the strings.}
# String are immutable

# 1. upper(){The upper() method converts a string to upper case.}

a = " !! Rishu!!!"
print(len(a))
print(a.upper())  # Rishu!!!
print(a)  # Rishu!!! becasue of immutable

# 2. lower(){The lower() method converts a string to lower case.}
print(a.lower())  # rishu!!!

# 3.strip() {The strip() method removes any white spaces before and after the string.}
print(a.strip())  # Rishu!!!

# 4. rstrip() {the rstrip() removes any trailing characters}
print(a.rstrip("!"))  # Rishu {not strip leading or front side}

# 5. replace() {The replace() method replaces all occurences of a string with another string.}
print(a.replace('Rishu', "john"))
# 6. split() {The split() method splits the given string at the specified instance and returns the separated strings as list items.}
print(a.split())  # ['!!', 'Rishu!!!']
# 7. capitalize() {The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.}
b = "introduction To js"
print(b.capitalize())

# 8. center() {The center() method aligns the string to the center as per the parameters given by the user}
c = "welcome to console"
print(len(c))
print(c.center(50))
# 9. count() { The count() method returns the number of times the given value has occurred within the given string.}
print(b.count("i"))  # 2

# 10. endswith() {The endswith() method checks if the string ends with a given value. If yes then return True, else return False.}
print(a.endswith("!!!"))
print(c.endswith("to", 4, 10))

# 11. find() {The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1}

d = "he name is dan. he is an honest man"
print(d.find("is"))  # 8
print(d.find("isss"))  # -1

# 12. index()  {The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.}

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# 13. isalnum() {The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.}
e = "welcometo001"
print(e.isalnum())
# 14. isalpha() {The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.}
print(e.isalpha())
# 15. islower() {The islower() method returns True if all the characters in the string are lower case, else it returns False.}
print(e.islower())  # True
# 16. isprintable() {The isprintable() method returns True if all the values within the given string are printable, if not, then return False.}
f = "this is printable \n"
print(f.isprintable())  # false
print(e.isprintable())
# 17. isspace() {The isspace() method returns True only and only if the string contains white spaces, else returns False.}
g = "  "
print(g.isspace())
# 18. istitle() {The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.}

h = "World health Organization"
print(h.istitle())
# 19. isupper() {The isupper() method returns True if all the characters in the string are upper case, else it returns False.}
print(h.isupper())
# 20. startswith() {The endswith() method checks if the string starts with a given value. If yes then return True, else return False.}
i = "python Is Good Programing languagage"
print(i.startswith("python"))
# 21. swapcase() {The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.}

print(i.swapcase())

# 22. title() {The title() method capitalizes each letter of the word within the string.}

print(i.title())
