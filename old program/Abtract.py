
# More oops concept in https://www.w3resource.com/python-exercises/oop/index.php

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectengle(shape):

    def __init__(self):
        self.length=5
        self.breadth=5
    def printarea(self):
       return self.length*self.breadth

class Circle(shape):
    
    def __init__(self,ar):
        self.r=ar
  
    # def printarea(self):
    #        return self.r*self.r

rect1=Rectengle()
cir=Circle(12)
print(rect1.printarea())
print(cir.printarea())
