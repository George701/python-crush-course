# A Dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members

# Create dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

#  Use constructor
person2 = dict(first_name='Sara', last_name='Williams')

print(person, type(person))
print(person2, type(person2))

#  Get value
print(person['first_name'])
print(person.get('last_name'))

#  Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
personNew = person.copy()
personNew['city'] = 'Boston'
print(personNew)

# Remove item
del(person['age'])
person.pop('phone')
#  Clear
person.clear()

# Get length
print(len(personNew))
print(person)

#  List dictionary

people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 32},
]

print(people[1]['name'])