""" for information
list=[]
dic={key:value}
set={}
generater=()
"""
#list comprehension

# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# print(ls)
# ls=[i for i in range(100) if i%3==0]
# print(ls)

#dic comprehension

# dict={i:f"item{i}" for i in range(1,100) if i%10==0}
# print(dict)

# dict={i:f"item{i}" for i in range(5)}
# dict1={value:key for key,value in dict.items()}

# print(dict,"\n",dict1)

#set com

# dress={dresses for dresses in ["gress1","gress2",
#                                 "gress1","gress2"]}
# print(dress)

# dress={"gress1","gress2", 
#         "gress1","gress2"}
# for Dresses in dress:
#     print(Dresses)


#generator com

even=(i for i in range(100) if i%2==0)
print(type(even))
print(even.__next__())
print(even.__next__())
#for i in even:
#  print(i)

#execise

# no_if_list=int(input("how many items you wants to add:"))
# list=[]
# for i in range(no_if_list):
#     llist=input("Enter your item:")
#     list.append(llist)
# while True:
#     select=int(input('''select your comprehension: \n 1.list \n 2.dict \n 3.set \n'''))
#     if select==1:
#      ls=[i for i in list]
#      print(ls)
#      print(type(ls))
#     elif select==2:
#      ls={f'item{i}': i for i in list}
#      print(ls)
#      print(type(ls))
#     elif select==3:
#      ls={i for i in list}
#      print(ls)
#      print(type(ls))
#     else:
#      print("Enter your number Between 1 to 3")





