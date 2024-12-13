class A:
    def met(self):
        print("class A")

class B(A):
    pass
    # def met(self):
    #    print("class B")
class C(A):
    def met(self):
        print( "class c")
class D(B,C):
    pass
   #def met(self):
       #print("clasa D")

a=A()
b=B()
c=C()
d=D()

d.met()