f=open("python.txt","r")
#print(f.read(5))
#print(f.read())
#print(f.readline())
for x in f:
    print(x)
"""
f=open("python.txt","rw")
f.write("this is overwrite upon old file")
f.close()
f=open("python.txt","r")
print(f.read())
"""
"""
f=open("python.txt","w")
f.write("This is last sentance")
f.close()
f=open("python.txt","r")
print(f.read())
"""
"""
f=open("myfile.txt","x")
f.write("THis is my new file")
f=open("myfile.txt","r")
print(f.read())
"""
"""
# to remove file we import os modual
import os
#os.remove("myfile.txt")

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("file dose not exists")
    """