import numpy as np
r=int(input("How maany raw you want to add:"))
c=int(input("How many columns you want to add:"))

list2=[]
for i in range(r):
    list1=[]
    for j in range(c):
       list1.append(int(input()))
    list2.append(list1)
print("mtrix 1")
list3=np.array(list2)
print(list3)
"""
for p in range(r):
    for q in range(c):
        print(list2[p][q],end="")
    print()
"""
    

                 

 

    
   
