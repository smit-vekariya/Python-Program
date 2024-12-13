#“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, 
#whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. 
import pickle

#pickling
car=["honda","mg","BMW"]
file="mycar.pkl"
fileobj=open(file,"wb")
pickle.dump(car,fileobj)
fileobj.close()


#unpickling
# fileobj=open("mycar.pkl","rb")
# unpic=pickle.load(fileobj)
# print(unpic)
# print(type(unpic))
