print("Project:Username Formatter")
name = input("Enter your full name: ")
first_chars = name[0:3]
print(first_chars)
last_chars = name[-3:]
print(last_chars)
rev = name[::-1]
print(rev)
jump = name[0::2]
print(jump)
var = name.find(" ")
print(name[0:var])
print(name[var+1:])
