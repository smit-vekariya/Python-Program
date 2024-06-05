list1=['a','b','c','d']

print("using enumerate")
for i in enumerate(list1):
    print(i)
    
print("using index")
for index,i in enumerate(list1 ,start=1):
    print(index,i)
    
print("find index")
l=list1.index('c')
print(l)