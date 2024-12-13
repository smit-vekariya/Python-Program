
try:
    f=open("smit_Exercise.txt","w")
    try:
        f.write("hii my name is smit")
    except:
        print("variable x is not define")
    finally:
        f.close()   
finally:
    print("this is fine")
    

# x=-1
# if x<0:
#     raise Exception("Sorry, no number  below Zero")


# x="hello World"
# if type(x) is not int:
#     raise Exception("THis is not int")
