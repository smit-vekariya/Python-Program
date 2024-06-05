#split list

import numpy as np
mylist=[1,2,3,4,5,6,7,8,9,0]
print(np.array_split(mylist,5))
"""
def splitt(mylist,chunk_size):
    length=len(mylist)
    for x in range(0,length,chunk_size):
        print("x", x)
        yield mylist[x:x+chunk_size]
        
mylist=[1,2,3,4,5,6,7,8,9,0]
chunk_size=2
print(list(splitt(mylist,chunk_size)))
"""