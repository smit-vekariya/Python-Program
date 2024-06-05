class Employee:
    no_leave=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary

    def printdetail(self):
        return f"Employee name is {self.name} and salary is {self.salary}."

    @classmethod
    def change_leave(cls,newleave):
        cls.no_leave=newleave

    def __add__(self,other):
        return self.salary+other.salary
    def __gt__(self,other):
        return self.salary>other.salary
    def __xor__(self,other):
            return self.salary^other.salary
    #for more dunder type mapping opreator to function in google

    def __str__(self):
        return f"Employee= {self.name} and salary = {self.salary}"

    def __repr__(self):
        return f"Employee : {self.name} and salary :{self.salary}"



    
emp1=Employee("smit",1200)
emp2=Employee("shah",1000)
Employee.change_leave(12)
print(emp1.printdetail())
print(Employee.no_leave)
print(repr(emp2))
print(emp1+emp2)
print(emp1>emp2)
print(emp1^emp2)