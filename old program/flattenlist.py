# 1 way

# from functools import reduce
# list1=[[1],[2,3],[4,5,6]]
# re=reduce(lambda x,y:x+y ,list1)
# print(re)

# 2 way

# list1=[[1],[2,3],[4,5,6]]
# list2=[j for i in list1 for j in i]
# print(list2)

# 3 way
# list1=[[1],[2,3],[4,5,6]]
# list3=[]
# for i in list1:
#     for j in i:
#         list3.append(j)
# print(list3)        

# 4 way
list1=[[1],[2,3],[4,5,6]]
list2 = []
for i in list1:
    list2 += i
