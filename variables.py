# A value container

'''
  comments
'''

"""
  Variable rules:
    - Variable names are case sensitive (name and Name are different variables)
    - Must start with a letter or a n underscore
    - Can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str
# is_cool = True  # boolean

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

print('Hello', x, y, name)

# Basic math

a = x + y

print(a)

# CheckType

print(type(a))

# Casting

a = str(a)

print(a, type(a))

x = str(x)
y = int(y)
z = float(y)

print(type(y), y)
print(type(z), z)