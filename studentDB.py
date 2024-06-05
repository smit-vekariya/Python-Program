
class StudentList:
    database = []
    
    @classmethod
    def append(cls, rno, name):
      cls.database.append({"roll_no":rno, "name":name})
    
    @classmethod 
    def insert(cls, rno, name, pos):
        database = cls.database
        res = list(filter(lambda database: database[1]["roll_no"] == pos , enumerate(database)))
        database.insert(res[0][0],{"roll_no":rno, "name":name})
        
    @classmethod
    def delete(cls, rno):
        cls.database = list(filter(lambda database : database["roll_no"] != rno, cls.database))
        
    @classmethod
    def edit(cls, rno):
        database = cls.database
        res = list(filter(lambda database: database["roll_no"] == rno , database))
        position = database.index(res[0])
        new_name = input("Please Enter new name:")
        database[position]["name"] = new_name
    
    @classmethod
    def search(cls, name):
        name_list = list(filter(lambda database: database["name"] == name , cls.database))
        for data in name_list:
           print(f"{data["roll_no"]} | {data["name"]}")
    
    @classmethod
    def display(cls):
        print("RollNo | Name")
        for data in cls.database:
           print(f"{data["roll_no"]} | {data["name"]}")


class ERP:
    def mainMenu():
        print("Welcome to the Linked Student List")
        print("************************")
        print("1. Add Student     5. Display Student")
        print("2. Insert Student  6. Search Student")
        print("3. Delete Student  7. Sort Student List")
        print("4. Edit Student    8. Save Student in File")
        print("9. Exit")
        print("************************")
        choice = int(input("Please Enter Your Choice:"))
        return choice 

s_list = StudentList()
while True:
    choice = ERP.mainMenu()
    if choice == 1:
        RollNo = input("Enter Roll No : ")
        Name = input("Enter Name : ")
        s_list.append(RollNo, Name)
    elif choice == 2:
        RollNo = input("Enter Roll No : ")
        Name = input("Enter Name : ")
        Position = input("Enter Roll No where you went to insert before : ")
        s_list.insert(RollNo, Name, Position)
    elif choice == 3:
        RollNo = input("Enter Roll No to delete : ")
        s_list.delete(RollNo)
    elif choice == 4:
        RollNo = input("Enter Roll No to edit : ")
        s_list.edit(RollNo)
    elif choice == 5:
        s_list.display()
    elif choice == 6:
        Name = input("Enter name to search : ")
        s_list.search(Name)
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        break
    else:
        print("Invalid Choice...")