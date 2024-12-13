class student:
    no_leaves=8
    def __init__(self,aname,aage):
        self.name=aname
        self.age=aage

    def printstudent(self):
        return f"The student name is {self.name} and age is {self.age}." 

    @classmethod
    def chenge_leave(cls,newleave):
       cls.no_leaves=newleave
    
    @staticmethod
    def static_method(no_leave_must):
        print(no_leave_must)

class player:
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame

    def printdetail(self):
        return f"The student name is {self.name} and age is {self.game}." 
 
class coolstudent(student,player):
    language="python"
    def printcool(self):
        print(self.language)



smit=student("vekariya",21)
amit=player("ranpariya",20)
karan=coolstudent("smit",11)
mal=smit.printstudent()
print(mal)
dal=amit.printdetail()
print(dal)
karan.printcool()
print(coolstudent.no_leaves)
print(karan.printstudent())


smit.chenge_leave(10)
print(smit.no_leaves,"====")

smit.static_method(11)

        