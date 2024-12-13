def convertfloat(list):
    list2=[]
    c=0
    for i in list1:
      list2.append(float(i))
    else:
      c=c+1
    print(f"{c} item can not convert in to float")
    print(list2)

list1=input("Enter the list: ").split()
convertfloat(list1)
