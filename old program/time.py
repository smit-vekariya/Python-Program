import time

whiletime=time.time()
print(whiletime)
k=0
while(k<10):
    print("this is while.")
    k+=1
    
print("after while loop",time.time()-whiletime)


fortime=time.time()
print(fortime)
for i in range(10):
    print("this is for")
print("after for loop",time.time()-fortime)


time.sleep(2)
print("this is sleep.")

localtime=time.asctime()
#localtime=(time.localtime(time.time()))
print(localtime)