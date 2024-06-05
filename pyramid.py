"""
for j in range(5):
    for i in range(j+1):
       print(i+1,end="")
    print()
"""
"""
for j in range(5):
    for i in range(j+1):
       print("*",end="")
    print()        
"""
"""
list1=['a','b','c','d']
p=len(list1)
for j in list1:
    for i in range(p):
       print(j,end="")
    p=p-1
    print()
"""
"""
ascii=65
for i in range(5):
    for j in range(i+1):
        a=chr(ascii)
        print(a,end="")
    ascii=ascii+1
    print()
"""
"""
n=5
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(" ",end="")
    k=k-1
    for p in range(i+1):
        print(" *",end="")
    print()
"""
"""
n=5
f=1
for i in range(0,n):
    for j in range(i+1):
        print(f ,end=" ")
        f=f+1
    print()
""" 