#  Create function
def sayHello(name = 'Sam'):
  print(f'Hello {name}')

sayHello()
sayHello('John Doe')

# Return values
def getSum(num1, num2):
  total = num1 + num2
  return total

num = getSum(3,4)
print(num)

getSumLambda = lambda num1, num2 : num1 + num2

print(getSumLambda(10, 2))