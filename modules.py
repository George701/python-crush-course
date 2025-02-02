'''
  A module is basically a file containing
    a set of functions to include in your application.
  There are core python modules,
    modules you can install using the pip package manager (including Django)
    as well as custom modules
'''

# Core modules
# import datetime
from datetime import date
# import time
from time import time

#  Pip module
from camelcase import CamelCase

#  import custom module
from validator import validate_email

# today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()
print(today, timestamp)

# pip install <module> installs everything globally
# pip freeze global

c = CamelCase()
print(c.hump('hello there world'))


email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')