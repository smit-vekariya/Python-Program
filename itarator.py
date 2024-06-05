class arraylist:
    def __init__(self,number):
        self.number=number
    def __iter__(self):
        self.pos=0
        return self
    def __next__(self):
        if (self.pos < len(self.number)):
            self.pos+=1
            return self.number[self.pos]
        else:
            raise StopIteration
            
x=arraylist([1,2,3])
y=iter(x)
print(next(y))
print(next(y))
#print(next(y)) Raise StopIteration
     
    
    