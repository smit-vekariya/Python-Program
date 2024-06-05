#pickel=that is use for convert pytho object to byte code( 0 or 1)
#unpickle==tyhat is use for back to convert byte code to python object
import pickle

pickle_off=open("picklefile.txt","rb")
print(pickle.load(pickle_off))