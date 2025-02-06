unsort = [2, 4, 6, 1, 34, 45, 22, 2, 1]
print("Unsorted:", unsort)

for index, data in enumerate(unsort):
    min = unsort[index]
    for i in range(index+1, len(unsort), 1):
        if unsort[index] > unsort[i]:
            unsort[index],  unsort[i]= unsort[i], unsort[index]
        
print("Sorted:", unsort)

