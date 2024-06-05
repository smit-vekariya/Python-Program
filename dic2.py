dic2={5:'a',2:'b',3:'c'}

for key,value in dic2.items():
    print(key,value)


for key in dic2:
    print(key,dic2[key])


for key in dic2.keys():
    print(key)
for value in dic2.values():
    print(value)

#sort dic by value
dic3=sorted(dic2.values())
print("dic2.values()", list(dic2.values()))
print(dic3)
#sort dic by key
dic4=sorted(dic2.keys())
print(dic4)