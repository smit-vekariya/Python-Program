
"""
def gen(n):
    for i in range(n):
        yield i
g=gen(20000)
print(g.__next__())
print(g.__next__())
print(g.__next__())

"""
"""
#gen in fibo

def fibogen(n):
    i1=0
    i2=1
    yield i1
    yield i2
    for i in range(n):
        f=i1+i2
        yield f
        i1=i2
        i2=f
g=fibogen(12)
#for i in g:
#  print(i)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

"""
"""
h="smit"
it=iter(h)
print(it.__next__())
print(it.__next__())
"""
# """
#factorial
def facgen(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        yield f
    print(f"final ans is {f}")

fg=facgen(5)
print(fg.__next__())
print(fg.__next__())
print(fg.__next__())
print(fg.__next__())
print(fg.__next__())


# """

'''
def fibo(x):
    p,q=0,1
    while(p<x):
        yield p
        p ,q=q,p+q
x=fibo(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())

for y in x:
    print(y)
'''
