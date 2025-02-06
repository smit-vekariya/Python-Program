unsorted = [2, 4, 6, 1, 34, 45, 22, 2, 1]
print("Unsorted:", unsorted)

for i in range(1, len(unsorted)):
    current_value = unsorted[i]
    j = i-1
    while j >= 0 and unsorted[j]> current_value:
        unsorted[j+1] = unsorted[j]
        j-=1
    unsorted[j+1] = current_value
        
print("Sorted:", unsorted)

