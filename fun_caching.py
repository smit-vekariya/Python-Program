"""
What does Functools lru_cache do?
Python's functools module comes with the @lru_cache decorator, 
which gives you the ability to cache the result of your functions using the Least Recently Used (LRU) strategy.
This is a simple yet powerful technique that you can use to leverage the power of caching in your code.
"""
import time
from functools import lru_cache


@lru_cache(maxsize=3, typed=True)
def some(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print("now runneing....")
    some(4)
    print("done")
   # input()
    some(4.0)
    print("calling again")
    
    
"""
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100000)))

print("before __name__ guard")
if __name__ == '__main__':
  functionA()
  functionB()
print("after __name__ guard")

"""