class library:
    def __init__(self,book_list,lib_name):
        self.book_list=book_list
        self.lib_name=lib_name
        self.landDict={}
        
    def display_book(self):
        print("OUR BOOKS:")
        for item in self.book_list:
            print(item)
   
    def land_book(self, user, landbook):
        if landbook not in self.landDict.keys():
            self.landDict.update({landbook:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.landDict[landbook]}")
            
    def add_book(self,addbook):
        self.book_list.append(addbook)
    def Returns_book(self,returnbook):
        self.landDict.pop(returnbook)        
            
if __name__=="__main__":
    smit=library(["cars","shaho","GOT","thums-up"],"smit_library")
    user=input("what is your name:")
    print("-------------------------------------------------")
    print(f"hello {user} to {smit.lib_name}:")
    print("-------------------------------------------------")
    while(True):
        print("SELECT OPTION:")
        print("1.Display book.")
        print("2.Land book.")
        print("3.Add book.")
        print("4.Return book.")
        print("5.Exit.")
        user_input=int(input("Enter your choice:"))
        if user_input not in [1,2,3,4,5]:
            print("Enter valid number:")
        if user_input==1:
            print("================================")
            smit.display_book()
            print("================================")
            #1
        elif user_input==2:
            print("================================")
            book_name=input("Enter book name that you want to land:")
            user_name=input("Enter your name:")
            smit.land_book(user_name,book_name)
            print("================================")
        elif user_input==3:
            print("================================")
            book_name=input("Enter book name that you want to add:")
            smit.add_book(book_name)
            print("================================")
        elif user_input==4:
            print("================================")
            book_name=input("Enter the book name that you want to returns:")
            smit.Returns_book(book_name)
            print("================================")
        elif user_input==5:
            exit()
        else:
            print("please enter valid number!!")
       #error     
    """print("Press 'q' for Exit and 'c' for continue")
    user_input2=""
    while(user_input2!="q" and user_input2!="c"):
        user_input2=input()
        if user_input2 =="q":
            exit()
        elif user_input2 =="c":
            continue
    """
    
  
    
    
          
            
    
            