str1="My Name is smit vekariya and I was studies in surat"
list1=(str1.split(" "))
list2=[]
for i in list1:
    p=i.lower()
    list2.append(p)

print(list2)
list2.sort()
for i in list2:
    print(i)