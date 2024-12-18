# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  def has_birthday(self):
    self.age += 1

# Init user object
brad = User('Brad Traversy', 'example@example.com', 37)
brad.has_birthday()
print(type(brad), brad)
print(brad.name)
print(brad.greeting())

#  Extend class

class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init customer
janet = Customer('Janet Smith', 'janet@example.com', 25)
janet.set_balance(500)
janet.has_birthday()
print(janet.greeting())