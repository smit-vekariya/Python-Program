class computer():
    def __init__(self):
        self.name="smit"
        self.age=21
    def update(self):
        self.age=30
        
c1=computer()
c1.name="vekariya"
print(c1.name) 
c2=computer()
print(c2.name)

c1.update()
print(c1.age)
print(c2.age)
if c1.age==c2.age:
    print("same")
else:
    print("not")