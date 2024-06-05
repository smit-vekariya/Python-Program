#filter=the filter method the given  sequence with helps of function 
#that test each element of the sequence to be true or not.
#syntex: filter(function,sequence)

# list1=[1,2,3,4,5,6,7,8,9,0]
list1=[{"sum_1":1},{"sum_2":2},{"sum_3":3}]

def grater_no(num):
    return int(list(num.values())[0]) == 2 

g=list(filter(grater_no,list1))
print(g)


#reduce
# from functools import reduce
# list1=[1,2,3,4,5]
# re=reduce(lambda x,y:print(x,y),list1)
# print(re)