class A:
    def __init__(self,name):
        self.name=name
        
class B(A):
    def __init__(self,fname,name):
        #A.name=name    #using parantclass
        #super(B,self).__init__(name) #using super 
        super().__init__(name)
        self.fname=fname
        
    def display(self):
        print(self.name, "and" ,self.fname)
    


obj=B("vekariya","smit")
obj.display()