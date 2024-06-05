class student:
    no_student=8
    def __init__(self,aname,aage):
        self.name=aname
        self.age=aage

    def printdedtail(self):
        print(f"Name is {self.name} and age is {self.age}.")

    @classmethod
    def from_dash(cls,string):
        nayan=string.split("-")
        print(nayan)
        return cls(nayan[0],nayan[1])
      #  return cls(*string.split("-"))

    @staticmethod
    def printstatic(string):
        print("ths is static method."+string)

smit=student("vekariya",12)
amit=student("ranpariya",13)
nayan=student.from_dash("padsala-10")
print(smit.printdedtail())
#print(nayan)
#print(student.printstatic("static"))