list_ = [10,27,69,27,25,17,78,26,79,26,98,67,6,1,4,82,93,97]

min = list_[0]
max = list_[0]
second_max = list_[0]
for i in list_:
    if min > i:
        min = i
    if second_max < max:
        second_max = i
    if max < i:
        max = i
    
print("min",min)
print("max", max)
print("second_max", second_max)
    