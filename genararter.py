#genarator
"""
def gen(str1):
    length=len(str1)
    for x in range(length):
        yield str1[x]
for y in gen("hello"):
    print(y)
"""
#2

mylist=[1,2,3,4]
a=(x**2 for x in mylist)
print(next(a))
print(next(a))

'''
#3
def fibo(nums):
    x,y=0,1
    for _ in range(nums):
        x,y=y,x+y
        yield x
def sq(nums):
    for num in nums:
        yield num**2
        
print(sum(sq(fibo(10))))
'''