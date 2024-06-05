def po(n):
    string="my name is smit"
  
    for index, i in enumerate(string):
       if(index==n):
         string.pop(index)
         print(string)
        
    
    
    
    
posi=int(input("Enter:"))
po(posi)