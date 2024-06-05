import os

class Student:
    def __init__(self, rno = 0, name = ""):
        self.RollNo = rno
        self.Name = name
        self.Next = None
        self.Previous = None

class MyList:
    def __init__(self):
        header = Student("RNo", "Name")
        self.start = header
        self.end = header

    def append(self, rno = 0, name = ""):
        newStudent = Student(rno, name)
        newStudent.Previous = self.end
        self.end.Next = self.end = newStudent

    def display(self):
        curr = self.start
        while curr is not None:
            print(f"{str(curr.RollNo)} | {curr.Name}")
            curr = curr.Next

    def insert(self, rno = 0, name = "", brno = 0):
        curr = self.start.Next
        while curr is not None and curr.RollNo != brno:
            curr = curr.Next        
        if(curr is not None and curr.RollNo == brno):
            newStudent = Student(rno, name)
            p = curr.Previous
            newStudent.Next = p.Next
            p.Next = newStudent
            newStudent.Previous = p
            curr.Previous = newStudent
            return 1
        else:
            return 0

    def remove(self, rno = 0):
        curr = self.start.Next
        while curr is not None and curr.RollNo != rno:
            curr = curr.Next
        if(curr is not None and curr.RollNo == rno):
            p = curr.Previous
            p.Next = curr.Next
            n = curr.Next
            n.Previous = p
            curr = None
            return 1
        else:
            return 0

    def update(self, rno = 0, name = ""):
        curr = self.start.Next
        while curr is not None and curr.RollNo != rno:
            curr = curr.Next        
        if(curr is not None and curr.RollNo == rno):
            curr.Name = name
            return 1
        else:
            return 0

slist = MyList()

def mainMenu():
    os.system('clear')
    print("Welcome to the Linked Student List\n")
    print("************************")
    print("1. Adding a New Student")
    print("2. Insert Student in List")
    print("3. Delete an Student")
    print("4. Edit an Student")
    print("5. Display Student List")
    print("************************")
    print("6. Exit")
    print("************************")
    choice = int(input("Please Enter your Choice : "))
    return choice

def addNewStudent():
    RollNo = input("Enter Roll No : ")
    Name = input("Enter Name : ")
    slist.append(RollNo, Name)

def insertBefore():
    RollNo = input("Enter Roll No : ")
    Name = input("Enter Name : ")
    bRollNo = input("Enter the Roll No before which to be inserted : ")
    if(slist.insert(RollNo, Name, bRollNo) == 0):
        input("Roll No To Be Inserted Before Does Not Exists ... ")

def deleteStudent():
    RollNo = input("Enter Roll No : ")
    if(slist.remove(RollNo) == 0):
        input("Roll No Does Not Exist ... ")

def editName():
    RollNo = input("Enter Roll No : ")
    Name = input("Enter New Name : ")
    if(slist.update(RollNo, Name) == 0):
        input("Provided Roll No Does Not Exists ... ")

def printAllStudentForward():
    slist.display()
    input("\n\nPress Enter to Return ...")

choice = 1
while choice != 6:
    choice = mainMenu()
    if choice == 1:
        addNewStudent()
    elif choice == 2:
        insertBefore()
    elif choice == 3:
        deleteStudent()
    elif choice == 4:
        editName()
    elif choice == 5:
        printAllStudentForward()
    elif choice == 6:
        pass
    else:
        input("Invalid Choice ... ")