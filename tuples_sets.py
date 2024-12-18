# A Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members

#  Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2, fruits == fruits2)

# If without comma, it becomes string
fruit_test = ('Apples')
fruit_test2 = ('Apples',)
print(type(fruit_test), type(fruit_test2))

#  Get values
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears' # Error

# Delete tuple
del fruits2
# print(fruits2)

#  Get length
print(len(fruits))

#  A Set is a collection which is unordered and unindexed.
# No duplicate members

#  Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#  Check if in set
print('Apples' in fruits_set)

#  Add to set
fruits_set.add('Grape')
print(fruits_set)
# It will not gonna add existing values
fruits_set.add('Apples')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete
# del fruits_set