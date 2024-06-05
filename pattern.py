num=int(input("how many number you want to add:"))
ch=int(input("type 1 or 0:"))
if ch==1:
    for i in range(0,num):
        for j in range(0,i+1):
           print("*",end="")
        print("\r")    
elif ch==0:
    for i in range(num,0,-1):
        for j in range(0,i):
          print("*",end="")
        print("\r")
else:
    print("Enter your choice between 1 or 0.")


# using recursion
# def pattern(a):
#     if a==0:
#         return
#     else:
#        pattern(a-1) 
#        print("*"*a)
#     #    pattern(a-1)
    
# pattern(5)