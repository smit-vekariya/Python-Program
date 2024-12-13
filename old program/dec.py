"""
def function1():
    print("i am smit.")
fun1=function1
fun1()

"""
def dec1(fun1):
   def second():
        print("this is second function")
        fun1()
        print("this is fun1")
   return second
@dec1
def function1():
    print("this is function")
#function1=dec1(function1)
function1()
