#*args

def args(a,b,*arg):
    print("arg", arg)
    mul=a*b
    for num in arg:
        mul*=num
    return mul
print(args(1,2,3,4,5))
print("================")

#*kwarg
def kwargs(**kwarg):
    print("kwarg", kwarg)
    for key,value in kwarg.items():
        print(f"{key}:{value}")

kwargs(arg1="smit verkariya",arg2="bhautik vekariya", arg3="parth vekariya")