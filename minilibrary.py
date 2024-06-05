class library:
    def __init__(self,list_book,name_lib):
        self.list_book=list_book
        self.name_lib=name_lib

    def display_book(self):
        print("OUR BOOKS:")
        for item in self.list_book:
            print(item)
  
    def add_book(self,books):
        self.list_book.append(books)
        print("your book Add suceesfully.")

    def lend_book(self,lendbook):
        if lendbook in self.list_book:
            self.list_book.remove(lendbook)
            print(f"Your '{lendbook}' are approved!!")
        else:
            print("book not aveliable!")



def system():
 try:
     value=True
     smit=library(["Harrypotter","GOT","Kickofmoon"],"smit_library")
     user_name=input("Enter your Name:")
     print(f"Welcome {user_name} to {smit.name_lib}:\n")
     while value==True:
         
         print("1:To Display book.")
         print("2:Add the book.")
         print("3:Lend the book")
         print("4:return the book")
         print("5:Exit")

         user_input=int(input("Enter your choice:"))

         if user_input==1:
             print(smit.display_book())
         elif user_input==2:
             new_book=input("Enter new book:")
             smit.add_book(new_book)
         elif user_input==3:
             book=input("Enter name of book of you want to lend:")
             smit.lend_book(book)
         elif user_input==4:
             return_book=input("Enter your book name for return:")
             smit.add_book(return_book)
             print(f"your Book {return_book} return succesfully!! Thanks..")
         elif user_input==5:
             value=False
         else:
             print("Wrong input..")
        
 except:
    print("Error!!!") 
    system()     
system()      







