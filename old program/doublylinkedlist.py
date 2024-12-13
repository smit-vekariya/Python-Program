import os
class student:
    def __init__(self,name="",roll=0):
        self.name=name
        self.roll=roll
        self.next=None
        self.pre=None
        
class LinkList:
    def __init__(self):
        header=student("Name","Roll")
        self.start=header
        self.end=header
    def append(self,name="",roll=0):
        newstudent=student(name,roll)
        newstudent.pre=self.end
        self.end.next=self.end=newstudent
    def display(self):
        temp=self.start
        while temp!=None:
            print(f"{str(temp.name)} : {temp.roll}")
            temp=temp.next
            
    def removestudent(self, rno = 0):
        temp = self.start.next
        while temp != None and temp.roll != rno:
            temp = temp.next
        if(temp!=None and temp.roll== rno):
            p = temp.pre
            p.next = temp.next
            n = temp.next
         #   n.pre = p
            temp = None
            return 1
        else:
            return 0
        
    def editstudent(self,name,rno):
        temp=self.start.next
        while temp!=None and temp.roll!=rno:
            temp=temp.next
        if(temp!=None and temp.roll==rno):
            temp.name=name
            return 1
        else:
            return 0
        
    def insert(self,name="",roll=0,rno=0):
        temp=self.start.next
        while temp!=None and temp.roll!=rno:
            temp=temp.next
        if(temp!=None and temp.roll==rno):
            newstudent=student(name,roll)
            p=temp.pre
            newstudent.next=p.next
            p.next=newstudent
            newstudent.pre=p
            temp.pre=newstudent
            return 1
        else:
            return 0
        
mylist=LinkList()
def add():
    s_Name=input("Enter Your Name:")
    s_Roll=int(input("Enter Your RollNo:"))
    mylist.append(s_Name, s_Roll)
    
def display():
    mylist.display()
    input("Press Enter to return.")
   
def insertbefore():
    name=input("Enter Your Name:")
    roll=int(input("Enter Your RollNo:"))
    rno=int(input("Enter your roll no before which to be inserted:"))
    mylist.insert(name,roll,rno)

def edit():
    s_name=input("Enter new name:")
    s_roll=int(input("Enter rollno:"))
    if(mylist.editstudent(s_name,s_roll)==0):
        input("Provided roll no does not Exits...")
        
def removest():
    s_roll=int(input("Enter RollNo for remove:"))
    if(mylist.removestudent(s_roll)==0):
        input("Roll No Does Exist.....")
        
def mainmanu():
    os.system('clear')
    print("Welcome to the Linked Student List")
    print("************************")
    print("1. Adding a New Student")
    print("2. Insert Student in List")
    print("3. Remove Student  from list.")
    print("4. Edit an student.")
    print("5. Display Student List")
    print("************************")
    print("6. Exit")
    print("************************")
    choice = int(input("Please Enter your Choice : "))
    return choice
  
choice=1
while choice!=6:
    choice=mainmanu()
    if choice==1:
        add()
    elif choice==2:
        insertbefore()
    elif choice==3:
        removest()
    elif choice==4:
        edit()
    elif choice==5:
        display()
    elif choice==6:
        pass
    else:
        print("invalid choice")