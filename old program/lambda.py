
list1=lambda x:x*5
print(list1(5))


list1=[1,2,3,4,5,6]
my=list(filter(lambda x:(x%2==0),list1))
print(my)



list1=[1,2,3,4,5,6]
my=list(map(lambda x:x*2,list1))
print(my)


my =lambda x,y:x+y
print(my(5,4))



def myfun(n):
    myfun2 =lambda x:x*n
    return myfun2
my=myfun(2)
print(my(3))