# try every programe to increse logic building

def pypart4(num):
    for i in range(num,0,-1):
        for j in range(0,i):
          print("*",end="")
        print("\r")
    
pypart4(5)

# =================================

# def pypart5(num):
#     for i in range(0,num):
#         for j in range(0,i+1):
#            print("*",end="")
#         print("\r")    
    
# pypart5(5)

# =================================

# def pypart2(n):
#     for i in range(n,0,-1):
#         for j in range(0, i):
#             # print(end="") # left side triangle
#             print(end=" ") # center triangle
#             # print(end="  ") # right triangle
#         new_n = (n - i) +1
#         for k in range(0, new_n):
#             print("* ",end="")
#         print("\r")

# pypart2(5)

# =================================

# def pypart3(a):
#     if a==0:
#         return
#     else:
#        pypart3(a-1) 
#        print("*"*a)
#     #    pypart3(a-1)
    
# pypart3(5)

# =================================

# def pattern5(a):
#     for i in range(0,a+1):
#         for j in range(1,i+1):
#            print(j,end="")
#         print("\r")
# pattern5(5)

# =================================

# def pypart6(n):
#     num =1
#     for i in range(n,0,-1):
#         for j in range(0, i):
#             # print(end="") # left side triangle
#             print(end=" ") # center triangle
#             # print(end="  ") # right triangle
#         new_n = (n - i) +1
#         for k in range(0, new_n):
#             print(num,end=" ")
#             num+=1
#         print("\r")

# pypart6(5)

# =================================

# def pattern3(a):
#     num=65
#     for i in range(0,a+1):
#         for j in range(1,i+1):
#             ch=chr(num)
#             print(ch,end=" ")
#             num=num+1
#         print("\r")
# pattern3(5)

# =================================

# def pattern3():
#     num=1
#     for i in range(65,70):  
#         for j in range(0,num):    
#             ch=chr(i)
#             print(ch,end="")  
#         print("\r")
#         num=num+1    
# pattern3()

# =================================
