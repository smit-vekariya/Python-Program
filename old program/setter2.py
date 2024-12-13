class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
      
    def explein(self):
        return f"Name is{self.fname} and surname is {self.lname}."
    @property
    def mail(self):
        if self.fname==None or self.lname==None:
            return "email not found!"
        else:
            return f"{self.fname}.{self.lname}@gmail.com."
  
    @mail.setter
    def mail(self,string):
        print("setting noww....")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @mail.deleter
    def mail(self):
        self.fname=None
        self.lname=None

raj_kundra=Employee("raj","kungra")
smit_patel=Employee("smit","patel")
print(raj_kundra.mail)

raj_kundra.fname="us"
print(raj_kundra.mail)

raj_kundra.mail="this.that@gmail.com"
print(raj_kundra.fname)

del raj_kundra.mail
print(raj_kundra.mail)