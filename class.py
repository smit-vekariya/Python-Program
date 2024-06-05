
class student:
    no_student=8
    def __init__(self,aname,aage):
        self.name=aname
        self.age=aage

    def printdetails(self):
        print(f"Name is {self.name} and age is {self.age}.")

    @classmethod
    def no_student_leave(cls,newleave):
        cls.no_student=newleave

smit=student("vekariya",12)
amit=student("ranpariya",13)
print(student.no_student)
print(smit.printdetails())
amit.no_student_leave(23)
print(student.no_student)
print(smit.no_student)
