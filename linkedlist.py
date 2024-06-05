class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def InsertLast(self,value):
        newnode=node(value)
        if( self.start==None):
            self.start=newnode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    def deleteFirst(self):
        if (self.start==None):
            print("list is empty.")
        else:
            self.start=self.start.next
    def views(self):
        if (self.start==None):
            print("list is empty.")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
mylist=LinkedList()
mylist.InsertLast(10)
mylist.InsertLast(20)
mylist.InsertLast(30)
mylist.InsertLast(40)
mylist.InsertLast(50)
mylist.InsertLast(60)
mylist.views()
print()
mylist.deleteFirst()
mylist.views()
        
            
            