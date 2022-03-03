

import functools
from timeit import repeat

def repeat(num_times):
  def decorator_repeat(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat
@repeat(num_times=6)
def greet(name):
  print(f'Hello {name}')

# greet('Nobert')

class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0

  def __call__(self, *args, **kwds) :

      self.num_calls += 1
      print(f'This is executed {self.num_calls} times')
      return self.func(*args, **kwds)
  
@CountCalls
def say_Hello():
  print("hello")

say_Hello()
say_Hello()
say_Hello()
say_Hello()
say_Hello()
