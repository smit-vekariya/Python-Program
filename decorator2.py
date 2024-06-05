def div(a,b):
    print(a/b)
    
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return a,b
    return inner


div=smart_div(div)
div(2,4) 
# to understand this is program watch  video number #44 of telusko chennal