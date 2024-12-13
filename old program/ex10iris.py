import requests
import pickle

data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#print(data)

#data2=data.split("\n")
#print(data2)

data3=[item.split(",") for item in data.split("\n") if len(item)!=0]
#print(data3)

"""
for item in data.split("\n"):
    if len(item)!=0:
        data4=item.split(",")
    print(data4)
"""
#make picklefile
"""
with open("mypickle.pkl","wb") as f:
    pickle.dump(data3,f)
"""
#from read pickle file:
with open("mypickle.pkl","rb") as f:
    print(pickle.load(f))