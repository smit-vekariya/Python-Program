f1=open("py.txt")
try:
    f=open("smit_Exercise.txt")
    #f=open("dose.txt")
except EOFError as e:
    print("EO error:",e)

except IOError as e:
    print("IO error:",e)

else:
    print("else running if except not ruuing.")
finally:
    print("run this anyway")
    #f.close()
    f1.close()

print("haha")

