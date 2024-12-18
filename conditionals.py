# if \ else

x = 20
y = 10

# Comparison operators (==, !=, >, <, >=, <=)

# Simple if
if x > y:
  print(f'{x} is greater than {y}')

# if/else
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{y} is greater than {x}')

# elif
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{y} is greater than {x}')

# Nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or)

# and
if x > 2 and x <= 10:
  print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
  print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'{x} is not equal to {y}')

# Membership Operator (not, not in)

numbers = [1,2,3,4,5]

# in
if x in numbers:
  print(x in numbers)

# not in
if x not in numbers:
  print(x not in numbers)

# Identity operators (is, is not)

# is
if x is y:
  print(x is y)

# is
if x is not y:
  print(x is not y)