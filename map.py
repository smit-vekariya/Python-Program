"""
lis=["121","12","13"]
number=list(map(int,lis))

#number[1]=number[1]+1
print(number[1])
""" 
#new
"""
number2=[1,2,3,4,5,6,7]
square=list(map(lambda x:x*x,number2))
print(square)
"""
#new

def sq(a):
    return a*a
def cube(a):
    return a*a*a
func=[sq,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)

