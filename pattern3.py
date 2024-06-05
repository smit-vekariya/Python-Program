# def pattern3(a):
#     for i in range(0,a+1):
#         for j in range(1,i+1):
#            print(j,end="")
#         print("\r")
# pattern3(5)

# =================================

def pattern3(a):
    num=1
    k=2*a
    for i in range(0,a+1):  
        for p in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i):
           print(num,end="  ")    
           num=num+1
        print("\r")
pattern3(5)

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
