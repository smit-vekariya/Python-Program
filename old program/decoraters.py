
# defining a decorator
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
         
    return inner1
# defining a function, to be called inside wrapper
@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")
 
 
# passing 'function_to_be_used' inside the
# decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)
 
# calling the function
function_to_be_used()
