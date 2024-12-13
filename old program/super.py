class A:
    classvar1="i am class veriable in class A."
    def __init__(self):
        self.var1="Constrater of class A."
        self.classvar1="instance variable in classs A"
        self.spaecial="special"

class B(A):
    classvar1="i am class variable in class B."
    def __init__(self):   
        
        #self.var1="Constrater of class B."
        self.classvar1="instance variable of class B."
        super().__init__()
        
a=A()
b=B()
print(b.spaecial)
print(b.var1)
print(b.classvar1)
print(a.var1)
