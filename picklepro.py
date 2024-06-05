#pickel=that is use for convert pytho object to byte code( 0 or 1)
#unpickle==tyhat is use for back to convert byte code to python object
import pickle

mylist=['a','b','c','d']
with open("picklefile.txt","wb") as fh:
    pickle.dump(mylist,fh)