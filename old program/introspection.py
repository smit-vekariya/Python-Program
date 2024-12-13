class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printdetail(self):
        return f"Name is {self.fname} and surename is {self.lname}."

    @property
    def mail(self):
        if self.fname==None or self.lname==None:
            return "email not found!"
        else:
            return f"{self.fname}.{self.lname}@gmail.com."
    @mail.deleter
    def mail(self):
        self.fname=None
        self.lname=None

smit=Employee("smit","vekariya")
jay=Employee("jay","patel")

print(jay.printdetail())
print(jay.mail)
del jay.mail
print(jay.mail)

"""
o="this is string"
print(dir(o))
#print(dir(smit))
"""


import inspect
print(inspect.getmembers(smit))
